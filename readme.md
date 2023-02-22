
# jc-ImgToIco

**Author**: [李俊才（Jack Lee）](https://github.com/jacklee1995)

**Version**: 0.0.1

**Email**: 291148484@163.com

**License**: MIT

**License Page**: [https://github.com/jacklee1995/jc-imgToIco/blob/master/LICENSE](https://github.com/jacklee1995/jc-imgToIco/blob/master/LICENSE)

**homepage**: [https://github.com/jacklee1995/jc-imgToIco](https://github.com/jacklee1995/jc-imgToIco)

---

<div id="chinese">
 
[English](#english) | [中文](#chinese)

# [中文文档](#chinese)

**将png、jpg等图片文件转换成ico图标的脚本工具。**

<div id="#1-2">

## [Python 版本](#1-2)

 - Python 3
 
 
<div id="#1-3">

## [用法](#1-3)

将你的所有 `png` 文件放在 更目录下的 `sources`目录下，在根目录下的 `config.ini` 配置文件中指定生成图标的大小。

在 Windows 系统上，你可以直接通过双击 `run.bat` 运行脚本启动图片转图标脚本，运行完成后，你可以在 `output` 目录中找到你的图标文件。 

配置文件大概包含以下内容：
```ini
[convert]
source_typr=.png    # .png or .jpg or all
output_size=128x128 
output_format=.ico  # .ico or .png or .jpg
```

其中 `output_size` 用于指定生成的 icon 大小。在该版本中，其他配置均不可用。

> **注意：**
>`.icon` 格式的图标文件只能是正方形，要求指定的长宽相等，常见的大小例如`16x16`、`32x32`、`64x64`、`128x128`、`256x256`等等。

---

<div id="english">
 
[中文](#chinese) | [English](#english)

# [English Document](#english)

**A scripting tool for converting png, jpg and other picture files into ico icons.**


<div id="#2-2">

## [Python version](#2-2)

 - Python 3

 
<div id="#2-2">

## [usage](#2-3)

Put all your `png` files in the  `sources` directory under the update directory, and specify the size of the generated icon in the `config.ini` configuration file under the root directory.

On the Windows system, you can start the script of image to icon directly by double-clicking `run.bat` to run the script. After running, you can find your icon file in the `output` directory.

The configuration file probably contains the following contents:

```ini
[convert]
source_typr=.png    # .png or .jpg or all
output_size=128x128 
output_format=.ico  # .ico or .png or .jpg
```

Here `output_size` is used to specify the generated icon size. No other configuration is available in this version.

> **note:** 
> the icon file in `.icon` format can only be square, and the specified length and width should be equal to sizes are as `16x16`、`32x32`、`64x64`、`128x128`、`256x256` etc.
