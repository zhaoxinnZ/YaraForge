[English] | [繁體中文](README_zh.md)
# YaraForge
YaraForge is an IDA Pro plugin for generating Yara rules from binary files. It utilizes the results of CAPA analysis to automatically generate corresponding Yara rules, helping security researchers and reverse engineers quickly identify and detect malware.

## Features

* Automatically extract key information from CAPA analysis results to generate Yara rules
* Support exporting detailed CAPA analysis results, including matched rules, addresses, etc.
* Save the generated Yara rules and related information to local files
* Provide a user-friendly interface for easy operation and configuration
* Built-in detailed logging functionality for troubleshooting and debugging

## Installation

1. Install YaraForge using pip:
```shell
pip install yaraforge
```
2. Copy the `yaraforge.py` file from the `yaraforge/plugin` folder to the `plugins` directory of IDA Pro.
3. Launch IDA Pro, and the YaraForge plugin will be loaded automatically.

## Usage

1. Open the target binary file in IDA Pro.
2. Run CAPA analysis to ensure that the analysis results are generated.
3. Use the `Ctrl+Y` shortcut or choose "Edit" -> "Plugins" -> "YaraForge" from the menu bar in IDA Pro to launch the plugin.
4. The plugin will automatically extract information from the CAPA analysis results and generate corresponding Yara rules.
5. The generated Yara rules and related information are saved by default in the `%APPDATA%\Hex-Rays\IDA Pro\plugins\yaraforge\` folder.
6. If you need to export the analysis results to the desktop, you can select the "Dump Caches on desktop" option in the plugin interface.

## Notes

* The YaraForge plugin relies on CAPA for analysis. When installing the plugin, CAPA will be automatically downloaded and installed, without the need for manual installation.
* The Yara rules generated by the plugin are for reference only and may need to be adjusted and optimized according to actual situations.
* Some functions of the plugin depend on the IDA Pro API, and there may be compatibility issues with different versions of IDA Pro. If you encounter any problems, please refer to the plugin's error logs and related documentation, or report them to us.

## Authors

* Zhao Xinn (zhaoxinzhang0429@gmail.com)
* Tsai YA-HSUAN (aooood456@gmail.com)
* Ting0525 (zg45154551@gmail.com)

## Special Thanks

We sincerely express our gratitude to [DuckLL](https://github.com/DuckLL), who has devoted considerable attention and patience to mentoring us. His substantial contributions and innovative ideas have significantly shaped the trajectory of this project.
## Version Requirements

* Python: >=3.8, <3.12
* CAPA: 7.0.1
* IDA Pro: >=7.0
* Windows 7/8/10/11

## License
* The YaraForge plugin is licensed under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.

## Acknowledgments
The development of the YaraForge plugin has received help and inspiration from many open-source projects and communities. We would like to express our gratitude to:

* CAPA: https://github.com/fireeye/capa
* Capstone: https://github.com/aquynh/capstone
* mkYARA: https://github.com/fox-it/mkYARA
* IDA Pro: The well-known commercial decompiler and debugger software

## Contact Us
If you encounter any issues while using the YaraForge plugin or have any suggestions and feedback, please feel free to contact us through the following channels:

* GitHub Issues: https://github.com/zhaoxinnZ/YaraForge/issues
* Email: zhaoxinzhang0429@gmail.com

Thank you for your support and attention! We hope that YaraForge can become a powerful assistant for your binary analysis and Yara rule generation.