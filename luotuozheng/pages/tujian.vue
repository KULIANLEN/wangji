<template>
	<view class="bigbox">
		<view class="title">
			装扮图鉴
			<image src="../static/tujian.png"  class="imagetop"></image>
		</view>
		<view class="backgroundcolor">
			
		</view>
		<view class="top">
			
		</view>
			
			<view class="middlebox">
				<view class="smallbox">
					<image src="../static/unlock_00000.png" class="image1"></image>
				</view>
				<view class="smallbox">
					
				</view>
				<view class="smallbox">
					
				</view>
				<view class="smallbox">
					
				</view>
				<view class="smallbox">
					
				</view>
				<view class="smallbox">
					
				</view>
				<view class="smallbox">
					
				</view>
				<view class="smallbox">
					
				</view>
				<view class="smallbox">
					
				</view>
			</view>
			<view class="middlebox2">
				<view class="image2">
					<image src="../static/shangyiye white.png" class="image2"></image>
				</view>
				
				<view class="image3">
					<image src="../static/nextwhite.png" class="image3"></image>
				</view>
			</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
	.middlebox2
	{
		display: flex;
		flex-direction: row;
		margin-top: 10vw;
		justify-content: space-around;
	}
	.image3{
		width: 15vw;
		height: 15vw;
		
	}
	.image2{
		width: 15vw;
		height: 15vw;
	}
	.image1{
		width: 22vw;
		height: 23vw;
	}
	.imagetop{
		width: 20vw;
		height: 21vw;
		position: absolute;
		top: 2vw;
		left: 6vw;
		z-index: -1;
	}
.title{
	margin-top: 10vw;
	margin-left: 20vw;
	font-size: 15vw;
	color:#e6e6fa;
}
.middlebox{
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
	margin-top: 10vw;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
	width: 94vw;
	margin-left: 3vw;
	
}
.smallbox{
	width: 22vw;
	height: 22vw;
	background-color: #f5f5f5;
	margin: 4vw;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
}
.backgroundcolor{
	background: linear-gradient(to   top,#FF6E53  , #FF6E52 0 , #FF8453 40% , #FF9758  ,#FFA859 );
	position: absolute;
	top: -10vw;
	width: 100vw;
	height: 100vh;
	z-index: -2;
}
.top{
	position: absolute;
	top: -10vw;
	
	width: 100vw;
	height:6vh;
	background: linear-gradient(to  bottom ,#FF6E53 0 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
	z-index: -2;
}
</style>