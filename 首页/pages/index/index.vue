<template>
  <view class="all">
	  
    
    <view class="zhongjian">
	  <view class="wenzi"></view>
      <button class="button"><span class="button-text1">图鉴</span></button>
      <button class="button"><span class="button-text1">二维码</span></button>
	  
	 
	 
      
    </view>
    <view class="di1">
		<view class="hh"></view>
		
		<button class="button3"><span class="button-text">邀请码</span></button>
		<button class="button4"><span class="button-text">抽卡</span></button>
		<button class="button5"><span class="button-text">我的订单</span></button>
	</view>
	<view class="di2">
		<view>兰大小萃版权所有</view>
	</view>
  </view>
</template>

<style>
.all {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.wenzi{
	
	height: 100%;
	border: 2px;
     font-size: 0rpx;
	 color: rgb(192, 192, 192);
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
	right: -60vw;

  
   top: 7vw;
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
 top:-8vw;
 left:20vw;
 height: 80px;
 width:80px;
 margin: 10px;
 background-color: #f1f1f1;
 border: none;
 cursor: pointer;
 border-radius: 50%;
 box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.2);
 transition: background-color 0.3s ease;
 color: #333;
}
.button4 {
	display: flex;
	align-items: center;
	justify-content: center;
  top: -10vw;
  bottom: 100vw;
  left:50vw;
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
  bottom:5vw;
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
.button2:before, .button3:before, .button4:before,.button5:before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 160px;
  height: 160px;
  background-color: orange;
  border-radius: 50%;
  animation-name: pulsate;
  animation-duration: 3.5s;
  animation-iteration-count: infinite;
  animation-timing-function: ease-in-out;
  opacity: 0;
}


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
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.button-text1 {
	font-size: 5rpx;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

</style>