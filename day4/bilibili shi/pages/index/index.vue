<template>
	
	<view class='bigbox'>
		<view class="item" v-for="(item,index) in question" :key="index">
			
			<image :src="convert(index)" style="width: 100%;height: 50%;" mode="aspectFill"></image>
			<view style="font-size: 4vw">{{item.answers[0].answer_text.substring(0,20)+'...'}}</view>
			<view style="color:#c2ccd0;font-size: 1vh;">{{item.answers[0].author}}</view>
			<view >
				<view></view>
				<view></view>
				<view></view>
				<view></view>
			</view>
	</view>
	<view class=smallbox>
		<image style="width: 5vw;
		height: 5vh;" src="../../images/shouye.png" mode=""></image>
		<image style="width: 5vw;
		height: 5vh;" src="../../images/shouye.png" mode=""></image>
		<image style="width: 5vw;
		height: 5vh;"src="../../images/shouye.png" mode=""></image>
	</view>
	</view>
</template>

<script>
	import questionAndAnswers from './qa.json'
	export default {
		data() {
			return {
				question:[]
			}
		},
		onLoad() {
			console.log(questionAndAnswers)
			this.question = questionAndAnswers
		},
		methods: {
			convert(index){
				index+=1
				if (index>8) index=index-6
				return require('../../images/lzu'+index+'.webp')
			}
		}
	}
</script>

<style>
	.images{
		width: 5vw;
height: 5vh;	}
	.content {
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
		
	}
	.item{
		display: flex;
		flex-direction: column;
		background-color:#ffffff;
		
		width: 45vw;
		height: 30vh;
		margin: 1vw;
		box-shadow: rgba(255, 255, 255, 0.1) 0px 1px 1px 0px inset, rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
		
		
	
	
	}
	.bigbox{
		display: flex;
		/* flex-direction: column; */
		flex-wrap: wrap;
		justify-content: space-between;
		width: 95vw;
		height: 90vh;
		/* height: 500px; */
		padding: 1vw;
		margin-bottom: 5vh;
		
	}
	.smallbox{
		display: flex;
		justify-content: space-between;
		
	}
</style>
