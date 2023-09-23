<template>
  <view class="all">
	  
    
    <view class="zhongjian">
	  <view class="wenzi1"> 小萃</view>
	  <view class="wenzi"> 骆驼证</view>
	


	  
      <button class="button"hover-class="hover1" @click="tujian"><span class="button-text1">图鉴</span></button>
      <button class="button"hover-class="hover1" @click="dianjichouka"><span class="button-text1">抽卡</span></button>
	  
	   
	  
	 
	 
      
    </view>
    <view class="di1">
		
		
		
		<button class="button3"hover-class="hover2" @click="dianji1"><span class="button-text1">邀请码</span></button>
		<button class="button4"hover-class="hover2" @click="dianjixjdd"><span class="button-text2">新建订单</span></button>
		<button class="button5"hover-class="hover2" @click="dianjimy"><span class="button-text">我的订单</span></button>
	</view>
	<view class="di2">
		<view>兰大小萃版权所有</view>
	</view>
	<view class='white' v-if='clicked'>
	
	</view>
  </view>
</template>
<script>
	export default {
  data() {
    return {
      isClicked: false,
	  clicked:false,
    };
  },
  methods: {
    onClick() {
      this.isClicked = !this.isClicked;
    },
	dianji1(){
		
		this.clicked=true,
		setTimeout(() => {
			uni.navigateTo({
				url:"/pages/yaoqing",
			}),
			this.clicked=false
		}, 500);
	},
	dianjichouka(){
		this.clicked=true,
		setTimeout(() => {
			uni.navigateTo({
				url:"/pages/chouka",
			}),
			this.clicked=false
		}, 500);
	},
	dianjixjdd(){
		this.clicked=true,
		setTimeout(() => {
			uni.navigateTo({
				url:"/pages/choose",
			}),
			this.clicked=false
		}, 500);
	},
	dianjimy(){
		this.clicked=true,
		setTimeout(() => {
			uni.navigateTo({
				url:"/pages/list",
			}),
			this.clicked=false
		}, 500);
	},
	tujian(){
		this.clicked=true,
		setTimeout(() => {
			uni.navigateTo({
				url:"/pages/tujian",
			}),
			this.clicked=false
		}, 500);
	}
  }
};
</script>

<style>
	.white{
		position: fixed;
		width: 100vw;
		height:100vh;
		margin-top: 0rpx;
	}
.all {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
.hover1 {
  transform: scale(1);
  transition: transform 0.3s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    background-image: linear-gradient(to right, #ff6e53, #ff8453);
    background-repeat: no-repeat;
    background-size: 200% auto;
    transition: background-position 0.3s ease;
	 transition: transform 0.3s ease;
	   transition: transform 0.3s ease, background-color 0.3s ease, color 0.3s ease;

}

.hover1:hover {
  transform: scale(1.1);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
   background-position: right center;
   transform: rotate(20deg);
    background-color: #ff6e53;
     color: #000;;
}
.hover2 {
  transform: scale(1);
  transition: transform 0.3s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    
    background-repeat: no-repeat;
    background-size: 200% auto;
    transition: background-position 0.3s ease;
	

}

.hover2:hover {
  transform: scale(1.1);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
   background-position: right center;
  
}
.wenzi{
	
	
	height: 100%;
	border: 2px;
     font-size: 100rpx;
	 font-weight: bold;

	 color: rgb(255, 255, 255);
	 font-family: '楷体';
	 margin-top: 15rpx;
}
.wenzi1{
	margin-left: 3vw;
	display: flex;
    align-items: center;
	
	height: 100%;
	border: 2px;
     font-size: 80rpx;
	 font-weight: bold;

	 color: rgb(255, 255, 255);
	 font-family: '楷体';
}
.daohang{
	height: 50rpx;
}
.hh{
	background: linear-gradient(to   right,#FF6E53 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
	height: 100rpx;
	background-color: darkorange;
	
	
}

.button {
	
	border-radius: 50%;
	right: -2vw;

  
   top: 3vw;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
	


  
  bottom: 10vw;
  height: 100rpx;
  width: 100rpx;
  margin: 10rpx;
  background-color: #f1f1f1;
  border: none;
  cursor: pointer;
  font-size: 30rpx;
  
  
  
}


.button3 {
display: flex;
	align-items: center;
	justify-content: center;
	
  
bottom: 40vw;
 top:-0vw;
 left:20vw;
 height: 80px;
 width:80px;
 margin: 10px;
 background-color: #f1f1f1;
 transition: background-color 0.3s ease;
 border: none;
 cursor: pointer;
 border-radius: 50%;
 box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.2);
 color: #333;
}
.button4 {
	display: flex;
	align-items: center;
	justify-content: center;
  top: -0vw;
  bottom: 100vw;
  left:60vw;
 height: 130px;
 width:130px;
  margin: 10px;
  background-color: #f1f1f1;
  border: none;
  cursor: pointer;
  border-radius: 50%;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease;
  color: #333;
}
.button5 {
  display: flex;
  align-items: center;
  justify-content: center;
  bottom:0vw;
  left:-20vw;
 height: 200px;
 width:200px;
  margin: 10px;
  background-color: #f1f1f1;
  border: none;
  cursor: pointer;
  border-radius: 50%;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.2);
  transition: background-color 0.3s ease;
  color: #333;
}


.button1:active,
.button2:active,
.button3:active,
.button4:active,
.button5:active,
.button:active {
  background-color: #ccc;
  transform: translateY(1px);
  transform: scale(1);
  transition: transform 0.3s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    background-image: linear-gradient(to right, #ff6e53, #ff8453);
    background-repeat: no-repeat;
    background-size: 200% auto;
    transition: background-position 0.3s ease;
  	 transition: transform 0.3s ease;
  	   transition: transform 0.3s ease, background-color 0.3s ease, color 0.3s ease;
  transform: scale(1.1);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
   background-position: right center;
   transform: rotate(20deg);
    background-color: #ff6e53;
     color: #000;;
}

.di1 {
  background-image: url("/static/666.jpg");
  height: 80vh;
  width: 100%;
  background-size: cover;
  background-position: bottom;
}
.di2{
	display: flex;
	justify-content: center;
	height: 20px;
	width: 100%;
	background-color: darkorange;
}
.di2 view{
	font-family: Zao Zi Gong Fang Yue Hei;
}
.zhongjian {
	
  background: linear-gradient(to   right,#FF6E53 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
  width: 100%;
  height: 150rpx;
  display: flex;
 
  
}
.button2, .button3, .button4 ,.button5{
  position: relative;
}
/* .button2:active, .button3:active, .button4:active,.button5:active {

 background-color: #f1f1f1;
 transition: background-color 0.3s ease;
} */


@keyframes pulsate {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 0;
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 0;
  }
}

.daohang {
  background-color: antiquewhite;
  width: 100%;
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  border-bottom: 1px solid #ccc;
}

.button-text {
	display: flex;
	flex-wrap: nowrap;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.button-text1 {
	font-size: 25rpx;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

</style>
