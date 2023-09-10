<template>
	<view>
		<nav class="navbar">
		  <div class="container">
		    <div class="logo">bilibii</div>
		    <ul class="nav-links">
		      <li><a href="#">首页</a></li>
					
		      <li><a href="#">推荐</a></li>
		      <li><a href="#">视频</a></li>
		      <li><a href="#">游戏</a></li>
		      <li><a href="#">音乐</a></li>
		      <li><a href="#">动画</a></li>
		    </ul>
		    <div class="search-bar">
		      <input type="text" placeholder="搜索">
		      <button><i class="fa fa-search"></i></button>
		    </div>
		  </div>
		</nav>
		<view class="wenti">
			<view class="qustion">{{qestionAndAnswer[showingIndex].question}}</view>
			<view class="answer">{{qestionAndAnswer[showingIndex].answers[0].author}} 2023-09-07 
未经作者授权，禁止转载</view>
		</view>
		<view>
		<image class="pic" src="../../static/image/1.png"></image>
		
		</view>
		<view>
		<image class="pic10" src="../../static/image/333.jpg"></image>
		
		</view>
		
		
		
		
	</view>
</template>

<script>
	import qa from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				qestionAndAnswer:[],
				showingIndex:0,
			}
		},
		
		onLoad() {
			
		},
		onShow() {
			this.qestionAndAnswer = qa
			console.log(this.qestionAndAnswer)
			this.showingIndex = this.$route.query.index;
			if(!this.showingIndex) this.showingIndex=0
			console.log(this.showingIndex)
		},
		methods: {
			
		}
	}
</script>

<style>
	.pic{
		
		width: 100vw;
		
		height: 50vh
		
		
		
		;
		
		
	}
	.pic1{width:40vw;
		  background-color: #00a1d6;
	}
	.kuang{  /* 在这里编写你的样式 */
		display:flex;
		background-color: #fffddd;
		border: 1px ;
		border-style: solid;
		padding: 10px;
		/* /* 更多样式属性... */
		height: 100px;
		align-items:flex-end
	}
  .ccc{
	  display: flex;
	  height: 50px;
  }
  .navbar {
    background-color: #00a1d6;
    color: #fff;
    transition: background-color 0.3s;
	width: 100vw;
  }
  
  .navbar:hover {
    background-color: #008bbf;
  }
  
  .container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0px 5px;
  }
  
  .logo {
    font-size: 24px;
    font-weight: bold;
    transition: color 0.3s;
  }
  
  .logo:hover {
    color: #f0f0f0;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
  }
  
  .nav-links li {
    margin-right: 20px;
    transition: transform 0.3s;
  }
  
  .nav-links li:hover {
    transform: scale(1.1);
  }
  
  .nav-links a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
  }
  
  .nav-links a:hover {
    color: #f0f0f0;
    text-decoration: underline;
  }
  
  .search-bar {
    display: flex;
    align-items: center;
  }
  
  .search-bar input[type="text"] {
    padding: 5px;
    border-radius: 5px;
    border: none;
  }
  
  .search-bar button {
    background-color: transparent;
    border: none;
    color: #fff;
    cursor: pointer;
    margin-left: 5px;
    transition: transform 0.3s;
  }
  
  .search-bar button:hover {
    transform: rotate(360deg);
  }
  
  /* 使用 Font Awesome 图标 */
  .fa-search:before {
    content: "\f002";
    font-family: FontAwesome;
  }
  .wenti{
	  text-align: center;
	  height: 80px;
	  font-size: 24px;
	  font-weight: bold;
	  background-color: white;
	  
  
  
  }
  .answer{
	  font-family: 'Courier New', Courier, monospace;
	  font-size: 15px;
	  padding: 10px;
	  background-color:white;
  }
  .pic8{
	  width: 100vw;
	  height: 100vh;
  }
  .qustion{
	  padding-top: 10px;
  }
  .pic10{
	  height: 100vh;
  }
</style>
