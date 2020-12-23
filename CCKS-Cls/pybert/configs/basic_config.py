
from pathlib import Path
BASE_DIR = Path('/home/LAB/liqian/test/game/Ori_graph/CCKS-Cls/pybert')
config = {
    'raw_data_path': BASE_DIR / 'dataset/train_sample.csv',
    'test_path': BASE_DIR / 'dataset/test.csv',

    'data_dir': BASE_DIR / 'dataset',
    'log_dir': BASE_DIR / 'output/log',
    'writer_dir': BASE_DIR / "output/TSboard",
    'figure_dir': BASE_DIR / "output/figure",
    'checkpoint_dir': BASE_DIR / "output/checkpoints",
    'cache_dir': BASE_DIR / 'model/',
    'result': BASE_DIR / "output/result",

    'bert_vocab_path': "/home/LAB/liqian/test/game/Ori_graph/pretrained_model/Bert-wwm-ext/bert_vocab.txt",
    'bert_config_file': '/home/LAB/liqian/test/game/Ori_graph/pretrained_model/Bert-wwm-ext/config.json',
    'bert_model_dir': "/home/LAB/liqian/test/game/Ori_graph/pretrained_model/Bert-wwm-ext"
}

