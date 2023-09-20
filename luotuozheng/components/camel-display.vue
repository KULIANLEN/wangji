<template>
	<view class="container">
		<image
		class="camel" 
		src="/static/images/camel/camel.png"
		mode="widthFix"></image>
		<image
		class="head"
		:src="headTexture"
		:style="'left:'+headOffsetX+'rpx;top:'+headOffsetY+'rpx;width:'+headWidth+'rpx;'"
		mode="widthFix"
		></image>
	</view>
</template>

<script>
</script>

<style>
	.container{
		position: relative;
		width: 100%;
		height: 100%;
		margin: 0;
		padding: 0;
		border: 0;
		background-color: transparent;
	}
</style>