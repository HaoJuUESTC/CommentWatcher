# 评论区监视器

顾名思义，为了防止b站评论区因为无删除记录造成的种种不便，制作了这个程序。

* API接口和软件原型参考[这里](https://github.com/GlobalCooling/get_bili_comments)，非常感谢
* 目前才开工，只有定期log功能
* 未来增加更多功能会考虑是否开源
* 如果评论为自行删除，请证明账号是你的（可以b站私信之类的），然后我会予以删除记录
* 禁止任何盈利用途
* 请勿用于违法乱纪行为，请勿滥用b站接口

---

目前针对 **咩2016** 的7则动态，一则视频进行抓取。评论区的oid就是文件夹名或者文件名。由于软件尚未完善，只抓到了5个小时左右的断续消息。
* 三个 `CommentWatcher` 开头的压缩包是通过js脚本爬取的，有一定的乱码和乱序
* `63148356.zip` 是只针对视频进行的抓取
* 有的地方会有整页缺失情况，应该是请求频率过高导致的
