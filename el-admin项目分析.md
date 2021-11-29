## 一、先大体来分析项目

> ==分析用到的技术栈==

- SpringBoot 2.1.0
- Vue
- Redis
- Swagger
- Spring-Data-Jpa（持久层框架）
- SpringSecurity
- JWT（Json Web Token）

> ==如果有Swagger，可以访问swagger==

里面有对应的api接口 全称Application Programming Interface，即应用程序编程接口。

> ==分析数据库==

数据库中的表有：

- code_column_config
- code_gen_config
- mnt_app
- mnt_database
- mnt_deploy
- mnt_deploy_history
- mnt_deploy_server

- mnt_server（服务）
- sys_dept（部门）
- sys_dict（字典）
- sys_dict_detail（字典细节）
- sys_job（工作）
- sys_log（日志）
- sys_menu（菜单）
- sys_quartz_job（）
- sys_quartz_log（）
- sys_role（角色）
- sys_roles_depts（部门和角色）
- sys_roles_menus（不同角色对应的菜单）
- sys_user（用户）
- sys_users_jobs（用户和工作）
- sys_users_roles（用户和角色的关系）
- tool_alipay_config（支付配置工具）
- tool_email_config（邮件配置工具）
- tool_local_storage （本地存储工具）
- tool_qiniu_config（七牛云配置工具）
- tool_qiniu_content（七牛云目录工具）

### 1.1、E-R图



## 二、前端登录页面

### 2.1、搭建工程

> ==升级npm，vue，node.js等的名命==

```cmd
node.js安装：https://www.runoob.com/nodejs/nodejs-install-setup.html
node.js下载地址为：https://nodejs.org/en/download/
注意：Linux 上安装 Node.js 需要安装 Python 2.6 或 2.7 ，不建议安装 Python 3.0 以上版本。
nodejs及npm升级到最新版本、指定版本
node有一个模块n，是专门用来管理node.js的版本的。
1、安装n模块：
npm install -g n
2、升级node.js到最新稳定版
n stable
3、安装指定版本：
n v6.11.5
#########################################################
npm 升级到最新版本
//
npm install -g npm
npm升级到指定版本
//比如升级到5.6.0
npm install -g npm@5.6.0
#########################################################
安装最新的vue
npm install -g vue-cli — 这个命令已经废弃了3.0以后
npm install -g @vue/cli
安装指定版本的vue
npm install -g @vue/cli@版本号
例如 ：
npm install -g @vue/cli@3.11.0
卸载vue
npm uninstall -g @vue/cli
#########################################################
vue项目element-ui升级到某版本
1.npm uninstall element-ui 卸载掉当前版本
2.npm install element-ui@2.3.9 -S 安装你想要的版本，
注意element-ui@2.3.9是一项，中间没有空格
3.最后在main.js中把default修改为theme-chalk
// import 'element-ui/lib/theme-default/index.css'
import 'element-ui/lib/theme-chalk/index.css'
#######################################################
全局配置淘宝镜像
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

> ==创建vue项目==

调出cmd输入(Vue 3及以上的新特性)

```cmd
vue ui
```

 ![image-20211107173128602](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107173136.png)

 ![image-20211107173621533](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107173621.png)

 ![image-20211107173709259](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107173709.png)

 ![image-20211107173717306](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107173717.png)

 ![image-20211107173849757](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107173849.png)

 ![image-20211107174035842](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107174035.png)

 ![image-20211107174044868](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107174044.png)

安装插件

 ![image-20211107180937873](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211107180939.png)



### 2.2、登录页面编写（主要还是CV大法）

1. 将自带的一些 组件(components) + 视图(views) 删除，然后添加自己的login.vue(在views下)

   ```vue
   <template>
       <div class="login" :style="'background-image:url('+ Background +');'">
         <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-position="left" label-width="0px" class="login-form">
           <h3 class="title">
             EL-ADMIN 后台管理系统
           </h3>
           <el-form-item prop="username">
             <el-input v-model="loginForm.username" type="text" auto-complete="off" placeholder="账号">
               <!-- <svg-icon slot="prefix" icon-class="user" class="el-input__icon input-icon" /> -->
             </el-input>
           </el-form-item>
           <el-form-item prop="password">
             <el-input v-model="loginForm.password" type="password" auto-complete="off" placeholder="密码" @keyup.enter.native="handleLogin">
               <!-- <svg-icon slot="prefix" icon-class="password" class="el-input__icon input-icon" /> -->
             </el-input>
           </el-form-item>
           <el-form-item prop="code">
             <el-input v-model="loginForm.code" auto-complete="off" placeholder="验证码" style="width: 63%" @keyup.enter.native="handleLogin">
               <!-- <svg-icon slot="prefix" icon-class="validCode" class="el-input__icon input-icon" /> -->
             </el-input>
             <div class="login-code">
               <img :src="codeUrl" @click="getCode">
             </div>
           </el-form-item>
           <el-checkbox v-model="loginForm.rememberMe" style="margin:0 0 25px 0;">
             记住我
           </el-checkbox>
           <el-form-item style="width:100%;">
             <el-button :loading="loading" size="medium" type="primary" style="width:100%;" @click.native.prevent="handleLogin">
               <span v-if="!loading">登 录</span>
               <span v-else>登 录 中...</span>
             </el-button>
           </el-form-item>
         </el-form>
         <!--  底部  -->
       <!--  <div v-if="$store.state.settings.showFooter" id="el-login-footer">
           <span v-html="$store.state.settings.footerTxt" />
           <span> ⋅ </span>
           <a href="https://beian.miit.gov.cn/#/Integrated/index" target="_blank">{{ $store.state.settings.caseNumber }}</a>
         </div> -->
       </div>
   </template>
   
   <script>
   // 引入背景
   import Background from '../assets/images/background.jpg'
   
   export default {
     name: 'Login',
     // 上面用到的数据
     data(){
       return{
         loginForm:{},
         loginRules:{},
         Background,
         codeUrl: '',
         loading: false
       }
     },
     methods: {
       // 获取
       getCode(){
   
       },
       handleLogin(){
   
       }
     }
   }
   </script>
   
   <style rel="stylesheet/scss" lang="scss">
     .login {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100%;
       background-size: cover;
     }
     .title {
       margin: 0 auto 30px auto;
       text-align: center;
       color: #707070;
     }
   
     .login-form {
       border-radius: 6px;
       background: #ffffff;
       width: 385px;
       padding: 25px 25px 5px 25px;
       .el-input {
         height: 38px;
         input {
           height: 38px;
         }
       }
       .input-icon{
         height: 39px;
         width: 14px;
         margin-left: 2px;
       }
     }
     .login-tip {
       font-size: 13px;
       text-align: center;
       color: #bfbfbf;
     }
     .login-code {
       width: 33%;
       display: inline-block;
       height: 38px;
       float: right;
       img{
         cursor: pointer;
         vertical-align:middle
       }
     }
   </style>
   

2. 注册路由（router下的index.js）

   ```javascript
   import Vue from 'vue'
   import VueRouter from 'vue-router'
   import Login from '../views/login.vue'
   Vue.use(VueRouter)
   
   const routes = [
     {
       path: '',
       name: 'Login',
       // 这个 component 是必须写的
       component: Login
     }
   ]
   
   const router = new VueRouter({
     mode: 'history',
     base: process.env.BASE_URL,
     routes
   })
   
   export default router
   
   ```

   

3. 添加到App.vue

   ```vue
   <template>
     <div id="app">
   	  <router-view></router-view>
     </div>
   </template>
   
   <script>
   
   export default {
     name: 'app',
     components: {
     }
   }
   </script>
   
   <style>
   #app {
     font-family: 'Avenir', Helvetica, Arial, sans-serif;
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
     text-align: center;
     color: #2c3e50;
     /* margin-top: 60px; */
   }
   </style>
   
   ```

   

4. 通过main.js渲染到 public下的index.html中（老祖宗）

   ```javascript
   import Vue from 'vue'
   import App from './App.vue'
   import router from './router'
   import store from './store'
   import './plugins/element.js'
   // global css
   import './assets/styles/index.scss'
   
   Vue.config.productionTip = false
   
   new Vue({
     router,
     store,
     render: h => h(App)
   }).$mount('#app')
   
   ```

   > ==效果图==

    ![image-20211108155705876](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108155706.png)

### 2.3、增加验证码功能

- 首先安装axios

  ```cmd
  npm install axios
  ```

- 在main.js (建议将需要用到的东西，全都在这里导入) 里引用并声明axios

  ```javascript
  import Vue from 'vue'
  import App from './App.vue'
  import router from './router'
  import store from './store'
  import Element from './plugins/element.js'
  // global css
  import './assets/styles/index.scss'
  import axios from 'axios' 
  
  // 只有第三方插件需要使用到 use
  Vue.use(Element)
  Vue.config.productionTip = false
  // 显示的绑定（prototype后面的名字可以随便起，只要自己记得住！）
  Vue.prototype.$request = axios
  
  new Vue({
    router,
    store,
    render: h => h(App)
  }).$mount('#app')
  
  ```

- 在login.vue里面去实现getCode方法

  ```javascript
  // 获取
  getCode(){
  // 利用axios发送请求给后端
  	this.$request.get('http://localhost:8000/auth/code').then(res => {
  		console.log(res);
  	});
  },
  ```

- 但是现在还不能点击验证码，所以我们需要写一个钩子函数（在 export 里）

  ```javascript
  // 创建一个钩子函数(自动调用验证码函数，因为默认是点击才会出现验证码的)
   created(){
     this.getCode();
   },
  ```

  > ==测试一下==

   ![image-20211108171558421](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108171600.png)

- 将验证码显示出来

  ```javascript
  // 获取
  getCode(){
  	// 利用axios发送请求给后端
  	this.$request.get('http://localhost:8000/auth/code').then(res => {
  		console.log(res);
  		// 赋值 注意这里不是this.loginForm.codeUrl
  		this.codeUrl = res.data.img;
  		// 这里赋值的是data里面含有的（但是并不是双向绑定的）
          this.loginForm.uuid = res.data.uuid;
  	});
  },
  ```

   ![image-20211108172515331](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108172515.png)

  
### 2.4、登录功能编写

#### 01、先获取Token

  - 在views下面新建一个Home.vue

    ```vue
    <template>
      <h2>Dashbord</h2>
    </template>
    
    <script>
    export default {
        name: "Dashbord",
    }
    </script>
    
    <style>
    
    </style>
    ```

     ![image-20211108174719193](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108174720.png)

  - 添加到路由index.js

    ```javascript
    import Vue from 'vue'
    import VueRouter from 'vue-router'
    import Login from '../views/Login.vue'
    Vue.use(VueRouter)
    
    const routes = [
      {
        path: '',
        name: 'Login',
        // 这个 component 是必须写的
        component: Login
      },
      {
        path: '/dashboard',
        name: 'Dashboard',
        // 懒加载，加快渲染速度
        component: () => import('../views/Home.vue')
      }
    ]
    
    const router = new VueRouter({
      mode: 'history',
      base: process.env.BASE_URL,
      routes
    })
    
    export default router
    
    ```

    

  - 编写handleLogin函数

    ```javascript
    // 登录请求
    handleLogin(){
    	this.$request.post('http://localhost:8000/auth/login',this.loginForm).then(res => {
    		console.log(res);
    	})
    }
    ```

- 这里后端需要先进行更改，因为现在前端没有加密，所以不需要解密

  - 最后效果图

  - ![image-20211108181745434](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108181747.png)


#### 02、进行路由跳转

可以理解为网页重定向

> ==思路==

<font color = 'red'>都是先导入路由(index.js)</font>  =>  <font color = 'bluee'>路由导出</font>  =>  <font color = 'gree'>把路由和App.vue导入main.js</font>  =>   <font color = 'podwer'>最后由main.js对index.html进行渲染</font>

此处应用的 $router,就是main.js里的router

 ![image-20211108215219973](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108215221.png)

修改handleLogin函数

```javascript
// 登录请求
handleLogin(){
    this.$request.post('http://localhost:8000/auth/login',this.loginForm).then(res => {
        // console.log(res);
        // 路由跳转 如果是history类型的，建议使用push，相当于栈（Stack），可以撤回
        this.$router.push('/dashboard');
    })
}
```

#### 03、密码加密功能编写

> ==概述==

前端会使用公钥进行加密，然后后端使用私钥进行解密（公钥和私钥可以去网站直接生成一对！）

- 先copy原工程的utils的**rsaEncrypt.js**

    ![image-20211108225915260](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108225916.png)

- 安装 **jsencrypt**

  ```cmd
  npm install jsencrypt --dep
  ```

- 将rsaEncrypt.js导入到Login.vue

  这里需要注意一下，由于ES6新规范，不是默认导出的（即export default XXX）,导入需要用 { XXX }

   ![image-20211108230439418](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211108230439.png)

  ```javascript
  // 登录请求
  handleLogin(){
      //加密  注意次加密类型只能针对字符串类型，数字型会为空
      this.loginForm.password = encrypt(this.loginForm.password);
      console.log(this.loginForm.password);
      this.$request.post('http://localhost:8000/auth/login',this.loginForm).then(res => {
          // console.log(res);
          // 路由跳转 如果是history类型的，建议使用push，相当于栈（Stack），可以撤回
          this.$router.push('/dashboard');
      })
  }
  ```

#### 04、增加表单校验

- 添加loginRules的属性

  ```javascript
  loginRules:{
      username: [{required: true, trigger: 'blur',message: '用户名不能为空！'}],
      password: [{required: true, trigger: 'blur',message: '密码不能为空！'}],
      code: [{required: true, trigger: 'blur',message: '验证码不能为空！'}]
  },
  ```

   ![image-20211109201906822](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211109201907.png)

-  ==效果图==![image-20211109200232641](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211109200241.png)

- 增加拦截功能

   ![image-20211109202146701](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211109202146.png)

    ![image-20211109203519487](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211109203519.png)

  > ==完善handleLogin的代码==

  ```javascript
  // 登录请求
  handleLogin() {
      this.$refs.loginForm.validate((valid) => {
          if (valid) {
              // 如果表单校验通过
              //加密  注意次加密类型只能针对字符串类型，数字型会为空
              this.loginForm.password = encrypt(this.loginForm.password);
              console.log(this.loginForm.password);
              this.$request
                  .post("http://localhost:8000/auth/login", this.loginForm)
                  .then((res) => {
                  // console.log(res);
                  // 路由跳转 如果是history类型的，建议使用push，相当于栈（Stack），可以撤回
                  this.$router.push("/dashboard");
              });
          } else {
              alert("请完善表单信息！");
          }
      });
  },
  ```

  > 
  >
  > ![image-20211109203654121](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211109203654.png)

#### 05、响应式拦截器

由于用户输错验证码后，前端用户无法直观的看到提示，所以我们需要进行设置拦截器，由于是在提交后，所以要用response，也就是响应式拦截器！

- 在utils文件夹下面创建request.js文件

  ```javascript
  import axios from "axios";
  import Element from "element-ui";
  
  let request = axios.create();
  
  // 因为是响应式 所以使用response
  request.interceptors.response.use(
      (response) => {
          console.log(response);
          // 一定要return回去
          return response;
      },
      (error) => {
          Element.Message.error("请求失败" + error);
          // 一定要return回去
          return Promise.reject(error);
      }
  );
  // 一定要进行导出
  export default request
  ```

   ![image-20211109213830514](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211109213832.png)

- 修改main.js

  ```javascript
  import Vue from 'vue'
  import App from './App.vue'
  import router from './router'
  import store from './store'
  import Element from 'element-ui'
  import 'element-ui/lib/theme-chalk/index.css'
  
  // global css
  import './assets/styles/index.scss'
  // 建议将需要用到的东西，全都在这里导入
  // import axios from 'axios'
  import request from '@/utils/request'
  
  // 只有第三方插件需要使用到 use
  Vue.use(Element)
  Vue.config.productionTip = false
  // 显示的绑定
  Vue.prototype.$request = request
  
  new Vue({
      router,
      store,
      render: h => h(App)
  }).$mount('#app')
  
  ```

  > ==效果图==

   ![image-20211109213856771](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211109213856.png)

### 2.5、记住我

> ==记住我本质上就是记住token==

接下来就是实现“记住我”功能了，其实就是JWT的前端实现。

token可以存储在storage或者cookies中，两者各有优点，相比之下存放在cookies更安全一些，这里采用的是cookies。

我们先来看看eladmin中是如何实现记住我功能的。

可以发现是比较复杂的，经过了层层封装，并且结合了Vuex的相关应用。



#### 01、拓展一下vuex的基础知识

> ==首先定义对象和请求==

store下的index.js

```javascript
state: {
    Fa: {id: 1, name: 'Ke ai fa', rank: 'p6', online: true},
    Jack: {id: 2, name: 'Jack Ma', rank: 'p10', online: true},
    Tony: {id: 3, name: 'Tony Ma', rank: 'p10', online: true},
    userCount: 3
  },
```

```javascript
 mutations: {
    // state 是状态，payload 是指前端传来的参数
    SET_RANK: (state, payload) => state.Fa.rank = payload,
    // 当然也可以直接写死
    SET_ONLINE: (state, payload) => state.Fa.online = false
  },
```

 ![image-20211111213350667](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211111213359.png)

> ==在login.vue里面调用==

 ![image-20211111213543369](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211111213543.png)

最后结果

 ![001](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211111213620.png)

> ==getters==

```javascript
// 相当于一个存储器（计算公式），减少代码的冗余
getters: {
    simpleHandle: (state) => {
        // 先去掉 p 获得纯数字
        let rankP = state.Fa.rank.replace("p","");
        let salary = Math.pow(2, rankP - 5) * 20;
        return salary + 'w';
    }
},
```

> ==Modules==

ModuleA.js

```javascript
const module = {
    state: {
        Fa_A: { id: 1, name: "Ke ai fa", rank: "p6", online: true },
        Jack_A: { id: 2, name: "Jack Ma", rank: "p10", online: true },
        Tony_A: { id: 3, name: "Tony Ma", rank: "p10", online: true },
        userCount_A: 3,
    },
    mutations: {
        // state 是状态，payload 是指前端传来的参数
        SET_RANK_A: (state, payload) => (state.Fa_A.rank = payload),
        // 当然也可以直接写死
        SET_ONLINE_A: (state, payload) => (state.Fa_A.online = false),
    },
    actions: {
        // injectee 相当于在vue组件使用 this.$store  因为这不是一个vue程序，所以无法直接使用
        setRank_A: (injectee, payload) => injectee.commit("SET_RANK_A", payload),
    },
    // 相当于一个存储器（计算公式），减少代码的冗余
    getters: {
        simpleHandle_A: (state) => {
            // 先去掉 p 获得纯数字
            let rankP = state.Fa_A.rank.replace("p","");
            let salary = Math.pow(2, rankP - 5) * 20;
            return salary + 'w';
        }
    }
}

export default module;
```

#### 02、记住我实战

在学习完Vuex的相关知识之后，我们就可以开始实现“记住我”功能了。

> ==传统的token（把token存到数据库中）==

 注意这是传统的token，JWT本身就包含校验信息，是不需要写入数据库的。

可以理解为：token是身份证号码，JWT是身份证，身份证上面是有过期时间的。

同时注意这种实现是完全基于Spring Security的，实际上前后端分离的时候不需要这样实现

![image](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211114224357.png)

> ==现在的Token==

 就是一种接力的方式，不需要存到数据库中

![image (1)](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211114224422.png)

> ==实现思路==

1. 保存用户名和密码到cookies
2. 保存token到cookies
3. rememberMe判断是否需要自动登录

由于token在登录、上传、部署等多个功能中都要用到，于是我们新建一个auth.js文件，定义公共的获取token和设置token的方法，供其他模块调用

```javascript
import Cookies from 'js-cookie'
import Config from '../settings'


const TokenKey = Config.TokenKey

export function getToken() {
    return Cookies.get(TokenKey)
}

export function setToken(token, rememberMe) {
    if (rememberMe) {
        // 存储天数默认是1天
        return Cookies.set(TokenKey, token, { expires: Config.tokenCookieExpires })
    } else return Cookies.set(TokenKey, token)
}

export function removeToken() {
    return Cookies.remove(TokenKey)
}

```

接着我们在发送登陆请求之后把token保存到Cookies里面

```javascript
this.$request
    .post("http://localhost:8000/auth/login", user)
    .then((res) => {
    // 发送登录请求后把token保存在Cookie里面
    setToken(res.data.token, user.rememberMe);
    // console.log(res);
    // 路由跳转 如果是history类型的，建议使用push，相当于栈（Stack），可以撤回
    this.$router.push("/dashboard");
});
```

那么关键来了，如何实现跳过登录页面？这就需要路由的基础知识了！

接下来再给大家介绍一下路由的基础知识。

跳过登录页面需要用到**导航守卫(NavigationGuard)**，在router/index.js中加入如下代码

```javascript
// 导航守卫
router.beforeEach((to, from, next) => {
    // 已登录
    if (getToken()) {
        // 如果要去的是登录页面，就跳到 首页
        if (to.name === "Login") next("/dashboard");
        // 放行
        else next();
    } 
    // 没有登录，且要去的不是登录页面
    else if(to.path !== "/") {
        // 跳到登录页面
        next({ path: "/" });
    }
    // 没有登录，但是要去的是登录页面
    else{
        next();
    }
});
```

这样就实现了“记住我”功能！

**其实记住我就是记住token，只要想办法把后端返回的token保存起来，就可以实现记住我了！**

### 2.6、注销功能

接下来我们来实现注销功能，首先我们去看下后端接口：

 ![image-20211115223456451](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211115223459.png)

然后根据这个后端接口来发送请求：Home.vue

```javascript
logout(){//请求后端接口删除该用户的token，同时前端Cookies也要删除该用户的token
    this.$request.delete('http://localhost:8000/auth/logout').then(res=>{    
        removeToken(Config.TokenKey)    
        this.$router.replace('/')  
    }
)}
```

注销功能部分完成！

### 2.7、请求拦截器（request）

细心的同学应该发现了，我所有对后端接口发送的请求都是**不带token**的，因为我们一直访问的都是不需要token就可以访问的接口（注销接口需要传token在后端对其进行删除，但不传也不会报错O(∩_∩)O），那么接下来如果我们要访问一些需要认证才允许访问的资源呢？

例如获取用户信息接口：auth/info

> ==request.js==

```javascript
// 请求式拦截器，request
request.interceptors.request.use(
    // 一定要注意 return 回去
    (config) => {
        console.log("请求拦截！");
        if (getToken()) {
            config.headers["Authorization"] = getToken();
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);
```

在Home.vue中加入如下代码：并在钩子函数中调用

```javascript
getUserInfo() {
    this.$request.get('http://localhost:8000/auth/info').then((res) => {
        console.log("获取用户信息!");
    });
},
```

可以发现返回状态码是401，也就是需要认证才能访问

那怎样在每个请求头之前加上token呢？很简单，用请求拦截器即可！

由于axios默认的请求格式就是application/json, 所以这里是不用设置的。

```javascript
// 请求式拦截器，request
request.interceptors.request.use(
    // 一定要注意 return 回去
    (config) => {
        console.log("请求拦截！");
        if (getToken()) {
            config.headers["Authorization"] = getToken();
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);
```

这样我们就在每次请求之前加上了token！

**注意：一定要记得return！因为use接受两个函数作为参数，那么这两个函数就必须要有返回值**

也可以理解为return就是拦截器放行，跟doFilter()作用类似。

### 2.8、请求等待

就是在用户填完表单后，登录按钮都变成登陆中了

```javascript
// 登录状态
this.loading = true;
```

在请求结束之后再设置为false即可

 ![image-20211116203440209](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211116203449.png)

### 2.9、认证失败（or 过期） 处理

不知道你们有没有发现，当重启电脑或者重启redis之后，就会卡在主页，既获取不到菜单，也无法跳转到登录页。那是因为浏览器Cookies中的token还没有过期，但是redis中已经没有该token了，所以就会导致以上的情况。

我们就来实现认证失败后的跳转功能~

需求：在认证失败之后，自动注销并跳转到登陆页面

 ![01](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211116203536.png)

首先，新建一个login.js里面可以封装一些与登录有关的方法

```javascript
import { removeToken } from "./auth";
import Config from '../settings';
import router from "../router";
import request from "./request";

export function logout() {
    // 请求后端接口删除该用户的token，同时前端Cookies也要删除该用户的token
    request.delete('http://localhost:8000/auth/logout').then((res) => {
        // 移除 token
        removeToken(Config.TokenKey);
        router.replace("/");
    });
}
```

接着在响应拦截器中添加代码：

```javascript
import { logout } from './login';

let code = error.response.data.status;
//如果认证失败，则实行注销操作
if( code===401){
    logout();
}
```

 ![image-20211116205506314](https://gitee.com/lovely-hair/blog-img/raw/master/img/20211116205508.png)

关闭redis再次访问主页，发现会自动跳转到登陆页面了！

好了，登录功能基本完善了！接下来我们去写主页面！
