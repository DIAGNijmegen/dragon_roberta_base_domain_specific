from dragon_baseline import DragonBaseline


class DragonRobertaBaseDomainSpecific(DragonBaseline):
    def __init__(self, **kwargs):
        """
        Adapt the DRAGON baseline to use the joeranbosma/dragon-roberta-base-domain-specific model.
        Note: when manually changing the model, update the Dockerfile to pre-download that model.
        """
        super().__init__(**kwargs)
        self.model_name = "joeranbosma/dragon-roberta-base-domain-specific"
        self.per_device_train_batch_size = 4
        self.gradient_accumulation_steps = 2
        self.gradient_checkpointing = False
        self.max_seq_length = 512
        self.learning_rate = 1e-05
        self.num_train_epochs = 5
        self.create_strided_training_examples = False


if __name__ == "__main__":
    DragonRobertaBaseDomainSpecific().process()
