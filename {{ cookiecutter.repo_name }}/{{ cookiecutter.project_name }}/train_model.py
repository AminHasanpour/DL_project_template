import datetime
from io import StringIO

import hydra
import omegaconf
import tensorflow as tf
import wandb
from wandb.keras import WandbCallback

from {{ cookiecutter.project_name }}.logger.easy_logger import get_logger
from {{ cookiecutter.project_name }}.data.get_data import get_data
from {{ cookiecutter.project_name }}.models.model import get_model


@hydra.main(config_name="config")
def main(cfg):
    # initializing
    logger = get_logger(__name__)
    
    wandb.init(mode="offline", project="{{ cookiecutter.project_name }}", name=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    wandb.config = omegaconf.OmegaConf.to_container(cfg, resolve=True, throw_on_missing=True)

    (train_x, train_y), (test_x, test_y) = get_data()   # USER: change this line respecting your application
    model = get_model()

    # model summary
    logger.info("model summary")
    with StringIO() as buf:
        model.summary(print_fn=lambda x: buf.write(x + '\n'))
        summary_str = buf.getvalue()
    logger.info(summary_str)

    # training
    logger.info("start training")

    if len(tf.config.list_physical_devices('GPU')) > 0:
        logger.debug("GPU is available")
    else:
        logger.debug("GPU is not available")

    opt = tf.keras.optimizers.Adam(learning_rate=cfg.learning_rate)
    model.compile(optimizer=opt, loss=..., metrics=...)     # USER: change this line respecting your application
    
    best_weights_path = "models/weights/weights_best/{time}/weights".format(time=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    best_weights_callback = tf.keras.callbacks.ModelCheckpoint(best_weights_path, save_best_only=True, save_weights_only=True, verbose=0)
    callbacks = [WandbCallback(), best_weights_callback]

    # USER: change this line respecting your application
    model.fit(train_x, train_y, epochs=cfg.epochs, batch_size=cfg.batch_size, validation_data=(test_x, test_y), callbacks=callbacks)

    # save the last and best model/weight
    model_last_path = "models/model_last/{time}/model.keras".format(time=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
    model.save(model_last_path)
    logger.info("model saved to {}".format(model_last_path))

    last_model_artifact = wandb.Artifact("last_model", type="model")
    last_model_artifact.add_file(model_last_path)
    wandb.log_artifact(last_model_artifact)

    best_model_artifact = wandb.Artifact("best_model", type="model")
    best_model_artifact.add_file(best_weights_path)
    wandb.log_artifact(best_model_artifact)

    # evaluate the last and best model
    logger.info("evaluating the last model")
    loss_last, acc_last = model.evaluate(test_x, test_y, verbose=0)         # USER: change this line respecting your application
    logger.info("loss: {:.6f}, acc: {:.6f}".format(loss_last, acc_last))    # USER: change this line respecting your application
    
    logger.info("evaluating the best model")
    model.load_weights(best_weights_path)
    loss_best, acc_best = model.evaluate(test_x, test_y, verbose=0)         # USER: change this line respecting your application
    logger.info("loss: {:.6f}, acc: {:.6f}".format(loss_best, acc_best))    # USER: change this line respecting your application

    wandb.finish()


if __name__ == "__main__":
    main()