<template>
	<view>
		<swiper class="swiper" circular indicator-dots autoplay interval=2000>
			<swiper-item>
				<image class="imag" src="../../static/logo.png"></image>
			</swiper-item>
			
			<swiper-item>
				<image class="imag" src="../../static/zhihu/tabbar/about.png"></image>
			</swiper-item>
			
			<swiper-item>
				<image class="imag" src="../../static/zhihu/tabbar/basics.png"></image>
			</swiper-item>
		</swiper>
		
		<view class="item" @click="click(index)" v-for="(item,index) in questionAndAnswers" :key="index">
			<view class="qustion">{{item.question}}</view>
			<view class="author">{{item.answers[0].author}}</view>
			<view class="answer">{{item.answers[0].answer_text.substring(0,20)+'...'}}</view>
		</view>
	</view>
</template>

<script>
	import questionAndAnswers from '../../data/zhihu/qa.json'
	export default {
		name:'zhihu',
		data() {
			return {
				questionAndAnswers:[]
			}
		},
		onLoad() {
			console.log(questionAndAnswers)
			this.questionAndAnswers = questionAndAnswers
		},
		created() {
			console.log(questionAndAnswers)
			this.questionAndAnswers = questionAndAnswers
		},
		methods: {
			click(index){
				console.log('zhihu',index)
				uni.navigateTo({
					url: '/pages/zhihu/browse?index='+index, // 参数名和值
				});
			}
		}
	}
</script>

<style>
	.imag{
		display:flex;
		width:200px;
		height:200px;
		margin: auto;
	}
	.swiper{
		display: flex;
		width: 100vw;
		height: 50vw;
	}
	.item{
		display: flex;
		width: 100vw;
		height: 20vw;
		padding: 1vw;
		background-color: aliceblue;
		margin-top: 1vw;
		flex-direction: column;
	}
	.qustion{
		display: flex;
		font-size: 4vw;
		font-weight: 20;
	}
</style>
