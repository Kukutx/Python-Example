# exe解包和重新打包_PyInstaller打包

![670d91d37d76994b592a1476c5d442be.png](https://img-blog.csdnimg.cn/img_convert/670d91d37d76994b592a1476c5d442be.png)

## [PyInstaller](https://so.csdn.net/so/search?q=PyInstaller&spm=1001.2101.3001.7020)打包

### 文件夹模式打包

```undefined
pyinstaller belle.py
```

项目文件夹下多出了三个文件(夹)，名称分别是build，dist和belle.spec，需要的可执行文件就在dist文件夹中。点击进入dist文件夹后，会发现有一个belle文件夹 ，这个文件夹就是需要的了————其中有可执行文件以及相关依赖。

### 单文件模式打包

所谓单文件模式打包就是打包后在dist文件夹中只有一个可执行文件，全部的依赖文件都已经被打包进去了。这样很方便，对不怎么懂编程或者电脑操作不是很熟练的客户来讲也比较友好。

要把belle.py打包成一个文件，只需要加一个-F命令：

```r
pyinstaller -F belle.py
```

打包成功后，我们在dist文件夹中运行生成的可执行文件。

### build, dist和spec文件(夹)简介

打包结束后，PyInstaller会在build文件夹中生成一些日志文件以及工作文件，而在dist文件夹中的是已经打包好的文件。spec文件中存储着打包时所用的命令以及要打包的相关文件，它的作用就是告诉PyInstaller如何来进行处理。

如果要给其他人使用： *若用文件夹模式打包，需要把打包好的整个belle文件夹发过去，其他人只需要点击文件夹中的belle.exe可执行文件即可运行程序。*
若用单文件模式打包，把dist文件夹下的belle.exe可执行文件发过去即可
build文件夹和spec文件跟程序运行没有关系，可以删掉。

------

## 黑框的调试作用以及如何去掉黑框

所谓黑框，其实就是命令行窗口。当成功打包并运行程序后，黑框中会显示程序输出内容。但是如果程序运行不成功，那黑框中就会显示报错信息，这个非常重要。而有些时候程序显示的是一个GUI界面，所以不想要黑框，不然用户会觉得不友好。 本小节会详细介绍如何利用黑框来调试，以及如何去掉黑框。

### 在黑框中查看报错信息

现在使用Python中自带的tkinter模块编写了一个简单的GUI界面，并设置了窗口的图标：

```haskell
import 
```

下载来之后我们将它放到项目路径下，命名为icon.ico。 接着用pyinstaller -F belle.py命令进行打包，打包成功后把图标文件拷贝到dist文件夹（即可执行文件文件路径下）中，进入dist文件并运行可执行文件就可以成功运行程序。 当程序运行出错的时候，黑框虽然会显示报错信息，但是可能会一闪而过。可以抓时机截图查看报错信息，或者可以用命令行运行可执行文件。

### 如何去掉黑框

去掉黑框其实非常简单，只需要加上-w命令即可：

```python
pyinstaller -F -w belle.py



import tkinter



 



# 创建主窗口



win = tkinter.Tk()



 



# 创建标签控件和按钮控件



label = tkinter.Label(win, text='Hello World')



btn = tkinter.Button(win, text='Button')



 



# 添加到主窗口中



label.pack()



btn.pack()



 



# 进入消息主循环



win.mainloop()
```

总之，在打包任何自带界面的程序时，建议先保留黑框，等确保打包和运行都没问题后，再加上-w命令重新打包下(除非特意要将黑框留下)。

------

## 给应用程序加上图标

本节了解如何给可执行文件加上自定义图标，并且解决一个常见的图标打包问题。

首先可以去这个网站下载一个ico格式的图标文件。

```undefined
注：在Mac上打包要下载.icns格式的图标文件。
```

将下载好的图标命名为smile.ico并放在项目路径下，接着直接在项目路径下打开命令行窗口输入以下打包命令：

```undefined
pyinstaller 
```

-i就是给程序添加图标的命令，需要在该命令后添加图标的路径，这个路径可以是相对路径，也可以是绝对路径：

```undefined
pyinstaller 
```

打包成功后，就可以在dist文件夹中看到加上了自定义图标的可执行文件。

```undefined
注：图标文件已经被打包进去，所以可以删掉，不会有关系。
```

### 为什么打包后图标不显示

打包图标时最常见的一个问题就是：明明我命令用的都对的，路径也对的，为什么打包后程序没有显示自定义图标？ 原因就是你的ico文件可能是无效的。很多人喜欢直接通过修改后缀名来获得一个ico文件，比如直接把.png修改成.ico。
这样操作的话很可能导致文件无效(即使能够打开)，所以最好借助专业的格式转换软件(比如格式工厂)来把其他格式的图片转为ico(或者.icns)格式的图标文件，或者可以在easyicon这个网站上寻找其他合适的图标。
也有可能是由于缓存的原因。其实是打包成功了，但在dist文件夹中还是没有显示。读者只需把生成的可执行文件拖到其他文件夹中(或直接拖到桌面上)就会发现图标显示正常。

------

## 其他基础命令

本节介绍PyInstaller的其他一些基础命令，有些很常用，另一些知道下就好。
-h，该命令可以显示PyInstaller的帮助信息，使用后可以看到所有PyInstaller命令的用法和解释。
-v，使用该命令可以查看当前所使用的PyInstaller的版本。
-D，文件夹模式打包，默认是文件夹模式，所以加与不加没有影响。
-n，使用该命令可以修改包含可执行文件的文件夹名称、可执行文件的名称以及spec文件的名称。

```r
# 这样可执行文件的文件夹名称、可执行文件的名称以及spec文件的名称都是run了



pyinstaller -n run belle.py
```

-y，当打包完毕后，我们可能会想修改下源码然后再次重新打包，那么第二次重新打包时 PyInstaller会询问是否要移除之前已经生成的文件。如果输入y，则删除并生成新文件；输入n则停止打包。但如果在第二次打包时加上-y命令的话(也就是不需要用户确认)，PyInstaller就会直接删除之前的文件(夹)然后打包生成新文件(夹)。

--distpath，使用该命令可以指定dist文件夹中可执行文件(及依赖)的生成路径，比方说笔者让dist文件夹中的内容在桌面上生成。

```sql
pyinstaller --distpath=D:/ belle.py
```

--workpath，该命令可以指定build文件夹中所有文件的生成路径，与--distpath同理。

--specpath，该命令指定spec文件的生成路径，同上。

--clean，在打包前先清理PyInstaller中的缓存并清除临时文件(如果要重新打包的话，建议加上该命令)

```css
pyinstaller --clean belle.py
```

既然涉及到删除，PyInstaller肯定会询问用户是否确认执行，可以加上-y命令。

```css
pyinstaller --clean -y belle.py
```

--hidden-import， 打包结束后，在运行时常常会碰到以下错误：

```vbnet
ModuleNotFoundError: No module named xxx
```

出现这种问题的原因无非就两种：

- 没有安装相应的模块，那么pip install xxx安装下即可
- 已经安装了，但PyInstaller在打包时没有找到，这时候可以使用该命令来解决(xxx即模块名称)：

```javascript
pyinstaller --hidden-import=xxx belle.py
```

或者可以直接选择在源码中import相应的模块，当然还可以修改spec文件来解决。

------

## spec文件

一个spec文件的例子。

```sql
block_cipher = None



a = Analysis(['minimal.py'],



    pathex=['/Developer/PItests/minimal'],



    binaries=None,



    datas=None,



    hiddenimports=[],



    hookspath=None,



    runtime_hooks=None,



    excludes=None,



    ciper=block_cipher)



pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)



exe = EXE(pyz, ...)



coll = COLLECT(...)
```

spec文件中主要包含4个class: Analysis, PYZ, EXE和COLLECT. *Analysis以py文件为输入，它会分析py文件的依赖模块，并生成相应的信息*
PYZ是一个.pyz的压缩包，包含程序运行需要的所有依赖 *EXE根据上面两项生成*
COLLECT生成其他部分的输出文件夹，COLLECT也可以没有

有时候PyInstaller自动生成的spec文件并不能满足需求，最常见的情况就是程序依赖本地的一些数据文件，这个时候就需要编辑spec文件来添加数据文件了。 上面的spec文件解析中Analysis中的datas就是要添加到项目中的数据文件，可以编辑datas。

```javascript
a = Analysis(



...



datas = [('you/source/file/path','file_name_in_project'),



    ('source/file2','file_name2')]



    ...



)
```

可以认为datas是一个List,每个元素是一个二元组。元组的第一个元素是你本地文件索引，第二个元素是拷贝到项目中之后的文件名字。除了上面那种写法，也可以将其提出来。

```erlang
added_files = [...]



a =Analysis(



    ...



    datas = added_files,



    ...



)
```

------

### 避免打包后包文件过大

为了避免 pyinstaller 打包后程序或文件夹过大，如：几百kb的程序打包后编程500M左右的程序，在引用包时，尽量使用 from ... import ... 语句，这是因为pyinstaller打包的路径其实是将python解释器以及项目中使用的库直接复制过来，所以如果你没事就 import... ，那么pyinstaller会将整个模块复制过去，此时打出来的包就会很大。

### 路径问题

使用python时，要养成使用 os.path.join 的习惯，这不仅可以避免跨平台的路径坑(windows路径表达与类Unix是不同)，又可以在打包时不会出现相对路径的问题，很多python程序员编写路径喜欢使用 + 号来链接路径，这会增加项目的维护成本。

### 外部数据问题

虽然在上节中，提及了使用外部数据时，可以自定义 spec 文件中的 datas 字段，但更常用的做法是直接将数据复制过去，不去修改datas。
比如项目中依赖 config 文件夹下的配置文件，执行将 config 文件夹整体直接复制到打包好的文件夹中则可。

### 加密问题

使用 pyinstaller 打包给他人使用时其实是不希望自己源代码被查阅或被修改的，而 pyinstaller 本身并没有加密功能。建议可以先使用cyphon后再用pyinstaller打包。