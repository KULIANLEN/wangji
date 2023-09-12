<template>
	<view>
		<!-- <view class="qustion">{{qestionAndAnswer[showingIndex].question}}</view> -->
		<view v-for="(item,index) in answers">
			<view>
				{{item.author}}
				{{item.answer_text}}
			</view>
		</view>
		<!-- <view class="answer">{{qestionAndAnswer[showingIndex].answers[0].author}}</view>
		<view class="answer">{{qestionAndAnswer[showingIndex].answers[0].answer_text}}</view> -->
	</view>
</template>

<script>
	import qa from '../../data/zhihu/qa.json'
	export default {
		data() {	
			return{
				answers: [
							{
								author:'0',
								answer_text:'0'
							},
							{
								author:'1',
								answer_text:'1'
							},
							{
								author:'2',
								answer_text:'2'
							}
					]
			}
			// return {
			// 	qestionAndAnswer:[],
			// 	showingIndex:0,
			
			
		},
		
		onLoad() {
			
		},
		// onShow() {
		// 	this.qestionAndAnswer = qa
		// 	// console.log(this.qestionAndAnswer)
		// 	this.showingIndex = this.$route.query.idx;
		// 	// if(!this.showingIndex) this.showingIndex=0
		// 	// console.log(this.showingIndex)
		// },
		methods: {
	
			
		}
	}
</script>

<style>

</style>
