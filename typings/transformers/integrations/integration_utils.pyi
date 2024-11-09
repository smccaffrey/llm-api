"""
This type stub file was generated by pyright.
"""

import comet_ml
from enum import Enum
from typing import Any, Dict, Literal, Optional, TYPE_CHECKING, Union
from ..utils import is_torch_available
from ..trainer_callback import TrainerCallback
from ..trainer_utils import BestRun

"""
Integrations with other Python libraries.
"""
logger = ...
if is_torch_available():
    ...
_MIN_COMET_VERSION = ...
_comet_version = ...
_is_comet_installed = ...
_is_comet_recent_enough = ...
if comet_ml.config.get_config("comet.api_key") is not None:
    _is_comet_configured = ...
else:
    _is_comet_configured = ...
_has_neptune = ...
if TYPE_CHECKING and _has_neptune:
    _neptune_version = ...
def is_wandb_available(): # -> bool:
    ...

def is_clearml_available(): # -> bool:
    ...

def is_comet_available(): # -> bool:
    ...

def is_tensorboard_available(): # -> bool:
    ...

def is_optuna_available(): # -> bool:
    ...

def is_ray_available(): # -> bool:
    ...

def is_ray_tune_available(): # -> bool:
    ...

def is_sigopt_available(): # -> bool:
    ...

def is_azureml_available(): # -> bool:
    ...

def is_mlflow_available(): # -> bool:
    ...

def is_dagshub_available(): # -> bool:
    ...

def is_neptune_available(): # -> bool:
    ...

def is_codecarbon_available(): # -> bool:
    ...

def is_flytekit_available(): # -> bool:
    ...

def is_flyte_deck_standard_available(): # -> bool:
    ...

def is_dvclive_available(): # -> bool:
    ...

def hp_params(trial): # -> dict[Any, Any]:
    ...

def run_hp_search_optuna(trainer, n_trials: int, direction: str, **kwargs) -> BestRun:
    ...

def run_hp_search_ray(trainer, n_trials: int, direction: str, **kwargs) -> BestRun:
    ...

def run_hp_search_sigopt(trainer, n_trials: int, direction: str, **kwargs) -> BestRun:
    ...

def run_hp_search_wandb(trainer, n_trials: int, direction: str, **kwargs) -> BestRun:
    ...

def get_available_reporting_integrations(): # -> list[Any]:
    ...

def rewrite_logs(d): # -> dict[Any, Any]:
    ...

class TensorBoardCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [TensorBoard](https://www.tensorflow.org/tensorboard).

    Args:
        tb_writer (`SummaryWriter`, *optional*):
            The writer to use. Will instantiate one if not set.
    """
    def __init__(self, tb_writer=...) -> None:
        ...
    
    def on_train_begin(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_log(self, args, state, control, logs=..., **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    


def save_model_architecture_to_file(model: Any, output_dir: str): # -> None:
    ...

class WandbLogModel(str, Enum):
    """Enum of possible log model values in W&B."""
    CHECKPOINT = ...
    END = ...
    FALSE = ...
    @property
    def is_enabled(self) -> bool:
        """Check if the value corresponds to a state where the `WANDB_LOG_MODEL` setting is enabled."""
        ...
    


class WandbCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that logs metrics, media, model checkpoints to [Weight and Biases](https://www.wandb.com/).
    """
    def __init__(self) -> None:
        ...
    
    def setup(self, args, state, model, **kwargs): # -> None:
        """
        Setup the optional Weights & Biases (*wandb*) integration.

        One can subclass and override this method to customize the setup if needed. Find more information
        [here](https://docs.wandb.ai/guides/integrations/huggingface). You can also override the following environment
        variables:

        Environment:
        - **WANDB_LOG_MODEL** (`str`, *optional*, defaults to `"false"`):
            Whether to log model and checkpoints during training. Can be `"end"`, `"checkpoint"` or `"false"`. If set
            to `"end"`, the model will be uploaded at the end of training. If set to `"checkpoint"`, the checkpoint
            will be uploaded every `args.save_steps` . If set to `"false"`, the model will not be uploaded. Use along
            with [`~transformers.TrainingArguments.load_best_model_at_end`] to upload best model.

            <Deprecated version="5.0">

            Setting `WANDB_LOG_MODEL` as `bool` will be deprecated in version 5 of 🤗 Transformers.

            </Deprecated>
        - **WANDB_WATCH** (`str`, *optional* defaults to `"false"`):
            Can be `"gradients"`, `"all"`, `"parameters"`, or `"false"`. Set to `"all"` to log gradients and
            parameters.
        - **WANDB_PROJECT** (`str`, *optional*, defaults to `"huggingface"`):
            Set this to a custom string to store results in a different project.
        - **WANDB_DISABLED** (`bool`, *optional*, defaults to `False`):
            Whether to disable wandb entirely. Set `WANDB_DISABLED=true` to disable.
        """
        ...
    
    def on_train_begin(self, args, state, control, model=..., **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, model=..., tokenizer=..., **kwargs): # -> None:
        ...
    
    def on_log(self, args, state, control, model=..., logs=..., **kwargs): # -> None:
        ...
    
    def on_save(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_predict(self, args, state, control, metrics, **kwargs): # -> None:
        ...
    


class CometCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [Comet ML](https://www.comet.com/site/).
    """
    def __init__(self) -> None:
        ...
    
    def setup(self, args, state, model): # -> None:
        """
        Setup the optional Comet integration.

        Environment:
        - **COMET_MODE** (`str`, *optional*, default to `get_or_create`):
            Control whether to create and log to a new Comet experiment or append to an existing experiment.
            It accepts the following values:
                * `get_or_create`: Decides automatically depending if
                  `COMET_EXPERIMENT_KEY` is set and whether an Experiment
                  with that key already exists or not.
                * `create`: Always create a new Comet Experiment.
                * `get`: Always try to append to an Existing Comet Experiment.
                  Requires `COMET_EXPERIMENT_KEY` to be set.
                * `ONLINE`: **deprecated**, used to create an online
                  Experiment. Use `COMET_START_ONLINE=1` instead.
                * `OFFLINE`: **deprecated**, used to created an offline
                  Experiment. Use `COMET_START_ONLINE=0` instead.
                * `DISABLED`: **deprecated**, used to disable Comet logging.
                  Use the `--report_to` flag to control the integrations used
                  for logging result instead.
        - **COMET_PROJECT_NAME** (`str`, *optional*):
            Comet project name for experiments.
        - **COMET_LOG_ASSETS** (`str`, *optional*, defaults to `TRUE`):
            Whether or not to log training assets (tf event logs, checkpoints, etc), to Comet. Can be `TRUE`, or
            `FALSE`.

        For a number of configurable items in the environment, see
        [here](https://www.comet.com/docs/v2/guides/experiment-management/configure-sdk/#explore-comet-configuration-options).
        """
        ...
    
    def on_train_begin(self, args, state, control, model=..., **kwargs): # -> None:
        ...
    
    def on_log(self, args, state, control, model=..., logs=..., **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_predict(self, args, state, control, metrics, **kwargs): # -> None:
        ...
    


class AzureMLCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [AzureML](https://pypi.org/project/azureml-sdk/).
    """
    def __init__(self, azureml_run=...) -> None:
        ...
    
    def on_init_end(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_log(self, args, state, control, logs=..., **kwargs): # -> None:
        ...
    


class MLflowCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [MLflow](https://www.mlflow.org/). Can be disabled by setting
    environment variable `DISABLE_MLFLOW_INTEGRATION = TRUE`.
    """
    def __init__(self) -> None:
        ...
    
    def setup(self, args, state, model): # -> None:
        """
        Setup the optional MLflow integration.

        Environment:
        - **HF_MLFLOW_LOG_ARTIFACTS** (`str`, *optional*):
            Whether to use MLflow `.log_artifact()` facility to log artifacts. This only makes sense if logging to a
            remote server, e.g. s3 or GCS. If set to `True` or *1*, will copy each saved checkpoint on each save in
            [`TrainingArguments`]'s `output_dir` to the local or remote artifact storage. Using it without a remote
            storage will just copy the files to your artifact location.
        - **MLFLOW_TRACKING_URI** (`str`, *optional*):
            Whether to store runs at a specific path or remote server. Unset by default, which skips setting the
            tracking URI entirely.
        - **MLFLOW_EXPERIMENT_NAME** (`str`, *optional*, defaults to `None`):
            Whether to use an MLflow experiment_name under which to launch the run. Default to `None` which will point
            to the `Default` experiment in MLflow. Otherwise, it is a case sensitive name of the experiment to be
            activated. If an experiment with this name does not exist, a new experiment with this name is created.
        - **MLFLOW_TAGS** (`str`, *optional*):
            A string dump of a dictionary of key/value pair to be added to the MLflow run as tags. Example:
            `os.environ['MLFLOW_TAGS']='{"release.candidate": "RC1", "release.version": "2.2.0"}'`.
        - **MLFLOW_NESTED_RUN** (`str`, *optional*):
            Whether to use MLflow nested runs. If set to `True` or *1*, will create a nested run inside the current
            run.
        - **MLFLOW_RUN_ID** (`str`, *optional*):
            Allow to reattach to an existing run which can be usefull when resuming training from a checkpoint. When
            `MLFLOW_RUN_ID` environment variable is set, `start_run` attempts to resume a run with the specified run ID
            and other parameters are ignored.
        - **MLFLOW_FLATTEN_PARAMS** (`str`, *optional*, defaults to `False`):
            Whether to flatten the parameters dictionary before logging.
        - **MLFLOW_MAX_LOG_PARAMS** (`int`, *optional*):
            Set the maximum number of parameters to log in the run.
        """
        ...
    
    def on_train_begin(self, args, state, control, model=..., **kwargs): # -> None:
        ...
    
    def on_log(self, args, state, control, logs, model=..., **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_save(self, args, state, control, **kwargs): # -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    


class DagsHubCallback(MLflowCallback):
    """
    A [`TrainerCallback`] that logs to [DagsHub](https://dagshub.com/). Extends [`MLflowCallback`]
    """
    def __init__(self) -> None:
        ...
    
    def setup(self, *args, **kwargs): # -> None:
        """
        Setup the DagsHub's Logging integration.

        Environment:
        - **HF_DAGSHUB_LOG_ARTIFACTS** (`str`, *optional*):
                Whether to save the data and model artifacts for the experiment. Default to `False`.
        """
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    


class NeptuneMissingConfiguration(Exception):
    def __init__(self) -> None:
        ...
    


class NeptuneCallback(TrainerCallback):
    """TrainerCallback that sends the logs to [Neptune](https://app.neptune.ai).

    Args:
        api_token (`str`, *optional*): Neptune API token obtained upon registration.
            You can leave this argument out if you have saved your token to the `NEPTUNE_API_TOKEN` environment
            variable (strongly recommended). See full setup instructions in the
            [docs](https://docs.neptune.ai/setup/installation).
        project (`str`, *optional*): Name of an existing Neptune project, in the form "workspace-name/project-name".
            You can find and copy the name in Neptune from the project settings -> Properties. If None (default), the
            value of the `NEPTUNE_PROJECT` environment variable is used.
        name (`str`, *optional*): Custom name for the run.
        base_namespace (`str`, *optional*, defaults to "finetuning"): In the Neptune run, the root namespace
            that will contain all of the metadata logged by the callback.
        log_parameters (`bool`, *optional*, defaults to `True`):
            If True, logs all Trainer arguments and model parameters provided by the Trainer.
        log_checkpoints (`str`, *optional*): If "same", uploads checkpoints whenever they are saved by the Trainer.
            If "last", uploads only the most recently saved checkpoint. If "best", uploads the best checkpoint (among
            the ones saved by the Trainer). If `None`, does not upload checkpoints.
        run (`Run`, *optional*): Pass a Neptune run object if you want to continue logging to an existing run.
            Read more about resuming runs in the [docs](https://docs.neptune.ai/logging/to_existing_object).
        **neptune_run_kwargs (*optional*):
            Additional keyword arguments to be passed directly to the
            [`neptune.init_run()`](https://docs.neptune.ai/api/neptune#init_run) function when a new run is created.

    For instructions and examples, see the [Transformers integration
    guide](https://docs.neptune.ai/integrations/transformers) in the Neptune documentation.
    """
    integration_version_key = ...
    model_parameters_key = ...
    trial_name_key = ...
    trial_params_key = ...
    trainer_parameters_key = ...
    flat_metrics = ...
    def __init__(self, *, api_token: Optional[str] = ..., project: Optional[str] = ..., name: Optional[str] = ..., base_namespace: str = ..., run=..., log_parameters: bool = ..., log_checkpoints: Optional[str] = ..., **neptune_run_kwargs) -> None:
        ...
    
    @property
    def run(self): # -> None:
        ...
    
    def on_init_end(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_train_begin(self, args, state, control, model=..., **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    def on_save(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_evaluate(self, args, state, control, metrics=..., **kwargs): # -> None:
        ...
    
    @classmethod
    def get_run(cls, trainer): # -> None:
        ...
    
    def on_log(self, args, state, control, logs: Optional[Dict[str, float]] = ..., **kwargs): # -> None:
        ...
    


class CodeCarbonCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that tracks the CO2 emission of training.
    """
    def __init__(self) -> None:
        ...
    
    def on_init_end(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_train_begin(self, args, state, control, model=..., **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    


class ClearMLCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [ClearML](https://clear.ml/).

    Environment:
    - **CLEARML_PROJECT** (`str`, *optional*, defaults to `HuggingFace Transformers`):
        ClearML project name.
    - **CLEARML_TASK** (`str`, *optional*, defaults to `Trainer`):
        ClearML task name.
    - **CLEARML_LOG_MODEL** (`bool`, *optional*, defaults to `False`):
        Whether to log models as artifacts during training.
    """
    log_suffix = ...
    _hparams_section = ...
    _model_config_section = ...
    _ignore_hparams_overrides = ...
    _ignoge_model_config_overrides = ...
    _model_config_description = ...
    _model_config_description_note = ...
    _train_run_counter = ...
    _model_connect_counter = ...
    _task_created_in_callback = ...
    _should_close_on_train_end = ...
    def __init__(self) -> None:
        ...
    
    def setup(self, args, state, model, tokenizer, **kwargs): # -> None:
        ...
    
    def on_train_begin(self, args, state, control, model=..., tokenizer=..., **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_log(self, args, state, control, model=..., tokenizer=..., logs=..., **kwargs): # -> None:
        ...
    
    def on_save(self, args, state, control, **kwargs): # -> None:
        ...
    


class FlyteCallback(TrainerCallback):
    """A [`TrainerCallback`] that sends the logs to [Flyte](https://flyte.org/).
    NOTE: This callback only works within a Flyte task.

    Args:
        save_log_history (`bool`, *optional*, defaults to `True`):
            When set to True, the training logs are saved as a Flyte Deck.

        sync_checkpoints (`bool`, *optional*, defaults to `True`):
            When set to True, checkpoints are synced with Flyte and can be used to resume training in the case of an
            interruption.

    Example:

    ```python
    # Note: This example skips over some setup steps for brevity.
    from flytekit import current_context, task


    @task
    def train_hf_transformer():
        cp = current_context().checkpoint
        trainer = Trainer(..., callbacks=[FlyteCallback()])
        output = trainer.train(resume_from_checkpoint=cp.restore())
    ```
    """
    def __init__(self, save_log_history: bool = ..., sync_checkpoints: bool = ...) -> None:
        ...
    
    def on_save(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    


class DVCLiveCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that sends the logs to [DVCLive](https://www.dvc.org/doc/dvclive).

    Use the environment variables below in `setup` to configure the integration. To customize this callback beyond
    those environment variables, see [here](https://dvc.org/doc/dvclive/ml-frameworks/huggingface).

    Args:
        live (`dvclive.Live`, *optional*, defaults to `None`):
            Optional Live instance. If None, a new instance will be created using **kwargs.
        log_model (Union[Literal["all"], bool], *optional*, defaults to `None`):
            Whether to use `dvclive.Live.log_artifact()` to log checkpoints created by [`Trainer`]. If set to `True`,
            the final checkpoint is logged at the end of training. If set to `"all"`, the entire
            [`TrainingArguments`]'s `output_dir` is logged at each checkpoint.
    """
    def __init__(self, live: Optional[Any] = ..., log_model: Optional[Union[Literal["all"], bool]] = ..., **kwargs) -> None:
        ...
    
    def setup(self, args, state, model): # -> None:
        """
        Setup the optional DVCLive integration. To customize this callback beyond the environment variables below, see
        [here](https://dvc.org/doc/dvclive/ml-frameworks/huggingface).

        Environment:
        - **HF_DVCLIVE_LOG_MODEL** (`str`, *optional*):
            Whether to use `dvclive.Live.log_artifact()` to log checkpoints created by [`Trainer`]. If set to `True` or
            *1*, the final checkpoint is logged at the end of training. If set to `all`, the entire
            [`TrainingArguments`]'s `output_dir` is logged at each checkpoint.
        """
        ...
    
    def on_train_begin(self, args, state, control, model=..., **kwargs): # -> None:
        ...
    
    def on_log(self, args, state, control, model=..., logs=..., **kwargs): # -> None:
        ...
    
    def on_save(self, args, state, control, **kwargs): # -> None:
        ...
    
    def on_train_end(self, args, state, control, **kwargs): # -> None:
        ...
    


INTEGRATION_TO_CALLBACK = ...
def get_reporting_integration_callbacks(report_to): # -> list[Any]:
    ...
