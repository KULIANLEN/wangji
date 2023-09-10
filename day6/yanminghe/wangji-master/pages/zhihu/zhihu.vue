<template>
	<view>
		<view class="item" v-for="(item,index) in questionAndAnswers" :key="index">
			<view class="qustion">{{item.question}}</view>
			<view class="author">{{item.answers[0].author}}</view>
			<view class="answer">{{item.answers[0].answer_text.substring(0,20)+'...'}}</view>
		</view>
	</view>
</template>

<script>
	import questionAndAnswers from '../../data/zhihu/qa.json'
	export default {
		data() {
			return {
				questionAndAnswers:[]
			}
		},
		onLoad() {
			console.log(questionAndAnswers)
			this.questionAndAnswers = questionAndAnswers
		},
		methods: {
			
		}
	}
</script>

<style>
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
