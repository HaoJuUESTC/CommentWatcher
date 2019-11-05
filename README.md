# 评论区监视器

顾名思义，为了防止b站评论区因为无删除记录造成的种种不便，制作了这个程序。

* API接口和软件原型参考[这里](https://github.com/GlobalCooling/get_bili_comments)，非常感谢
* 最近才开工，只有定期log功能
* 未来增加更多功能会重新考虑是否开源
* 如果评论为**自行删除**，麻烦证明一下账号是你的（如b站私信我），然后我尽量及时会删除记录
* **禁止任何盈利用途**
* **请勿用于违法乱纪行为，请勿滥用b站接口**

---

目前针对 **咩2016** 的7则动态，一则视频进行抓取。评论区的oid就是文件夹名或者文件名。由于软件尚未完善，只抓到了5个小时左右的断续消息。
* `old` 文件夹内部是较老的文件归档，会陆续整理
* 三个 `CommentWatcher` 开头的压缩包是通过js脚本爬取的，有一定的乱码和乱序
* oid命名的zip文件是持续性的抓取，这个目前会实时更新
    - 格式：oid-ctime-防重名数字
    - 时间排序应该以ctime为准，Python 中运行 `time.ctime(<ctime>)` 就能转换成实际时间
    - 目前由于没有服务器持续跑以及程序不稳定，时间跨度较大
* 有的地方会有整页缺失情况，应该是请求频率过高导致的
* 目前 ~~刚健朴实~~ 较为原始的删评获取方法是:在 Sublime Text 里打开两个文件，选中较早的按下 `Ctrl+Shift+P` 输入 `Compare with` ，再选择另一个进行比对。主要参照是 uid 和 ctime，因为文本可能出现乱码，用户可能改名

# 点下面查看所有疑似删评记录
* [视频av63148356](/AllDeletes/63148356.md)
* [动态“最后一条说明” ](/AllDeletes/40928079.md)
* [动态“补充”]()
* [动态“说明一下（我现在大概了解事情的经过了...)”](/AllDeletes/40870151.md)
