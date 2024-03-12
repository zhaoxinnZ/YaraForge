from pathlib import Path
import idaapi

plugin_path = Path(idaapi.get_user_idadir()) / "plugins"


metadata = {
    "plugin_name": "YaraForge",
    "plugin_dir_name": "yaraforge",
    "authors": [
        {"name": "Zhao Xinn", "email": "zhaoxinzhang0429@gmail.com"},
        {"name": "Tsai YA-HSUAN", "email": "aooood456@gmail.com"},
        {"name": "Ting0525", "email": "zg45154551@gmail.com"},
    ],
    "github_url": "https://github.com/zhaoxinnZ/YaraForge",
    "description": "A plugin for IDA Pro to generate Yara rules from binary files.",
    "python_requires": ">=3.9",
    "IDAPython_requires": ">=7.0",
    "capa_version": "7.0.1",
}

yaraforge_base_dir = plugin_path / metadata['plugin_dir_name']

pathnames = {
    "yaraforge_dir": yaraforge_base_dir,
    "cache_dir": yaraforge_base_dir / "cache",
    "results_dir": yaraforge_base_dir / "cache/results",
    "pretty_dump_dir": yaraforge_base_dir / "cache/results/pretty_dump",  # 添加 pretty_dump_file 的路徑
    "instructions_dir": yaraforge_base_dir / "cache/results/instructions",
    "yara_rules_dir": yaraforge_base_dir / "cache/results/yara_rules",
    "logger_dir": yaraforge_base_dir / "logs",
}
