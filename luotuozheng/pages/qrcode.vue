<template>
	<view class="a">
		<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
		<view class="top">
			<view class="biaoti">
				<text class="title" >{{title}}</text>
			</view>
		</view>
		<view class="middlebox">
			<img :src="imageUrl" class="qrcode">
		</view>
		<view class="text-area">
			<text class="sentence">{{sentence}}</text>
		</view>
		<view class="bottom">
			<img :src="background" class="tupian">
		</view>
		<ul class="bg-bubbles">
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
		</ul>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imageUrl: '',
				sentence: '请凭此二维码领取骆驼证',
				background: '/static/a.png',
				title: '二维码页面',
				icon:'/static/hhh/jiantou.png',
			}
		},
		mounted() {
			uni.request({
				url: '/api/getImage',
				method: 'GET',
				success: (res) => {
					
					this.imageUrl =
						'https://img9.vilipix.com/picture/pages/regular/2023/04/30/15/111427875_p0_master1200.jpg?x-oss-process=image/resize,m_fill,w_1000'
				},
				fail: (err) => {
					console.error(err);
				}
			});
		},
		methods :{
			fanhui(){
				uni.navigateTo({
					url:'/pages/index'
				})
			}
		},
	}
</script>
<style>
	.zuoshang {
		position: fixed;
		margin-top: 36rpx;
		margin-left: 15rpx;
	}
	
	.qrcode {
		height: 42vh;
		width: 42vh;
		display: flex;
		align-self: flex-end;
	}
	.icon {
		height: 4vh;
		width: 4vh;
		display: flex;
		justify-content: flex-start;
	}
	
	.a {
		display: flex;
		flex-direction: column;
		height: 100vh;
		width: 100vw;
	}

	.middlebox {
		height: 45vh;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 2;
		padding-top: 5.5vh;
	}
	.title{
		display: flex;
		justify-content: center;
		align-content: center;
		color: #ffffff;
	}
	.sentence {
		color: #c0c0c0;
		font-size: 25rpx;
		margin-top: 0%;
	}
	.text-area {
		height: 3vh;
		display: flex;
		justify-content: center;
		margin-top: 10px;
	}
	.top{
		width: 100vw;
		height:9vh;
		z-index: -2;
		background: linear-gradient(to   right,#FF6E53 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
		display: flex;
		justify-content: center;
		align-items: center;

	}
	.bottom{
		height: 40vh;
		bottom: 0;
		position: fixed;
	}
	.tupian{
		height: auto;
		position: fixed;
		width: 100vw;
		bottom: 0%;
	}
	.bg-bubbles {
	  position: fixed;
	  top: 0;
	  left: 0;
	  width: 100%;
	  height: 100%;
	  z-index: -1;
	}
	.bg-bubbles li {
	  position: absolute;
	  list-style: none;
	  display: block;
	  width: 40px;
	  height: 40px;
	  background-color: rgba(255, 255, 255, 0.35);
	  bottom: -160px;
	  -webkit-animation: square 25s infinite;
	  animation: square 25s infinite;
	  transition-timing-function: linear;
	}
	.bg-bubbles li:nth-child(1) {
	  left: 10%;
	}
	.bg-bubbles li:nth-child(2) {
	  left: 20%;
	  width: 80px;
	  height: 80px;
	  -webkit-animation-delay: 2s;
	          animation-delay: 2s;
	  -webkit-animation-duration: 17s;
	          animation-duration: 17s;
	}
	.bg-bubbles li:nth-child(3) {
	  left: 25%;
	  -webkit-animation-delay: 4s;
	          animation-delay: 4s;
	}
	.bg-bubbles li:nth-child(4) {
	  left: 40%;
	  width: 60px;
	  height: 60px;
	  -webkit-animation-duration: 22s;
	          animation-duration: 22s;
	  background-color: rgba(255, 255, 255, 0.45);
	}
	.bg-bubbles li:nth-child(5) {
	  left: 70%;
	}
	.bg-bubbles li:nth-child(6) {
	  left: 80%;
	  width: 120px;
	  height: 120px;
	  -webkit-animation-delay: 3s;
	          animation-delay: 3s;
	  background-color: rgba(255, 255, 255, 0.4);
	}
	.bg-bubbles li:nth-child(7) {
	  left: 32%;
	  width: 160px;
	  height: 160px;
	  -webkit-animation-delay: 7s;
	          animation-delay: 7s;
	}
	.bg-bubbles li:nth-child(8) {
	  left: 55%;
	  width: 20px;
	  height: 20px;
	  -webkit-animation-delay: 15s;
	          animation-delay: 15s;
	  -webkit-animation-duration: 40s;
	          animation-duration: 40s;
	}
	.bg-bubbles li:nth-child(9) {
	  left: 25%;
	  width: 10px;
	  height: 10px;
	  -webkit-animation-delay: 2s;
	          animation-delay: 2s;
	  -webkit-animation-duration: 40s;
	          animation-duration: 40s;
	  background-color: rgba(255, 255, 255, 0.5);
	}
	.bg-bubbles li:nth-child(10) {
	  left: 90%;
	  width: 160px;
	  height: 160px;
	  -webkit-animation-delay: 11s;
	          animation-delay: 11s;
	}
	@-webkit-keyframes square {
	  0% {
	    transform: translateY(0);
	  }
	  100% {
	    transform: translateY(-700px) rotate(600deg);
	  }
	}
	@keyframes square {
	  0% {
	    transform: translateY(0);
	  }
	  100% {
	    transform: translateY(-700px) rotate(600deg);
	  }
	}

</style>