<template>
	<view class="bigbox">
		<view class="top">
			
		</view>
		<view class="titlebox">
			<text class="title">请选择</text><br>
			<text class="title2">要创建的骆驼种类</text>
		</view>
		<view class="middlebox">
			<view class="smallbox">
				
			</view>
			<view class="smallbox">
				
			</view>
		</view>
		<view class="backgroundcolor">
			
		</view>
	</view>
</template>

<script>
</script>

<style>
	.top{
		position: absolute;
		top: -10vw;
		
		width: 100vw;
		height:6vh;
		background: linear-gradient(to  bottom ,#FF6E53 0 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
		z-index: -2;
	}
	.backgroundcolor{
		width: 100vw;
		height: 100vh;
		z-index: -2;
		background: linear-gradient(to   top,#FF6E53  , #FF6E52 0 , #FF8453 40% , #FF9758  ,#FFA859 );
		position: absolute;
		top: 0%;
	}
	.titlebox{
		margin-top: 10vw;
		margin-left: 20vw;
	}
	.title2{
		
		font-size: 8vw;
	}
	.title{
		text-align: center;
		font-size:15vw;
	}
</style>