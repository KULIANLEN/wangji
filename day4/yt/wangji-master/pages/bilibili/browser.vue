<template>
	<view>
		<view class="qustion">{{qestionAndAnswer[showingIndex].question}}</view>
		<view class="answer"></view>
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

</style>
