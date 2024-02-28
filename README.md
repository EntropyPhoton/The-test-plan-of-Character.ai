# The-test-plan-of-Character.ai
象际软件的Interview Project: The test plan of Character.ai
## Character.ai的核心功能
Character.ai是一个可以可以让用户自由创建AI角色，并与它们聊天，以此打造社交生态的网站。因此该网站最核心的功能就是**让用户和AI角色聊天**，也就是维持如图所示的聊天框正常运行。  
  ![Character.ai聊天界面](https://i0.hdslb.com/bfs/article/ef7d4b3066f615d3c74cbff790446e219fb51430.jpg@.webp)
其他的功能，例如创建多角色聊天室，分享聊天过程，社区动态都是围绕上述核心功能进行的
## 我所发掘的测试点  
对于一个网站进行测试，测试的大类一般如下：  
* **功能测试**
* **界面可用性测试**
* **兼容性测试**
* **接口测试**
* **安全测试**
* **性能测试**
* 由于Character.ai是B/S架构，因此还需要进行压力测试，检验服务器在大量用户访问时网站的稳定性
1. 首先，对于一个网站而言，第一项测试就是能否顺利连接到网站。  
2. 然后，当成功连接到网站之后，应该确保网站的界面可见，控件可用。  
3. 其次，对于Character.ai的新用户而言，网站上的所有功能都是需要先登录才能进行的。所以为了新用户能顺利开展后面的体验，保证用户注册和登录的可靠性是第一要务。  
  
综上所述，我认为最重要的前三点测试，应该是：
* **针对网站主页面的链接测试**
* **针对网站主页面的界面可用性测试**（比如主页的控件能否正确显示与使用）
* **针对网站登录和用户注册的功能测试**（其中包含了对登录界面的链接测试，表单的提交所需要的数据库测试，第三方登录网站的接口测试等）  
## 测试思路
