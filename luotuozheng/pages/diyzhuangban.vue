<template>
	<view>
	<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
	<view class="bigbox">
		<view class="top">
			<view class="backcolor">
				
				<!-- <view class="middlebox1">
					
				</view> -->
				
				<view class="middlebox2">
					<view class="smallbox">
						<button class="topbutton" @click="jump1()">装扮图鉴</button>
					</view>
					<view class="smallbox">
						<button class="topbutton" @click="jump2()">去抽卡</button>
					</view>
					<view class="smallbox">
						<button class="topbutton" @click="jump3()">填写信息</button>
					</view>
				</view>
				<view class="middlebox3">
					
				</view>
				<view class="middlebox4" v-show="page===1">
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					
					
				</view>
				<view class="middlebox4" v-show="page===2">
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					
					
				</view>
				<view class="middlebox4" v-show="page===3">
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					
					
				</view>
				<view class="middlebox4" v-show="page===4">
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					<view class="image">
						
					</view>
					
					
				</view>
				<view class="middlebox5">
					
					<view class="smallbox2">
						<button @click="change(1)" class="underbutton">1</button>
					</view>
					<view class="smallbox2" @click="change(2)">
						<button class="underbutton" >表情</button>
					</view>
					<view class="smallbox2" @click="change(3)">
						<button class="underbutton">帽子</button>
					</view>
					<view class="smallbox2" @click="change(4)">
						<button class="underbutton">坐垫</button>
					</view>
					
					
				</view>
			</view>
		</view>
		<!-- <view class="backcolor">
			
			<view class="middlebox1">
				
			</view>
			
			<view class="middlebox2">
				<view class="smallbox">
					<button class="topbutton">1</button>
				</view>
				<view class="smallbox">
					<button class="topbutton">2</button>
				</view>
				<view class="smallbox">
					<button class="topbutton">3</button>
				</view>
			</view>
			<view class="middlebox3">
				
			</view>
			<view class="middlebox4">
				<view class="image">
					
				</view>
				<view class="image">
					
				</view>
				<view class="image">
					
				</view>
				<view class="image">
					
				</view>
				
				
			</view>
			<view class="middlebox5">
				<view class="smallbox2">
					<button class="underbutton">1</button>
				</view>
				<view class="smallbox2">
					<button class="underbutton">2</button>
				</view>
				<view class="smallbox2">
					<button class="underbutton">3</button>
				</view>
				<view class="smallbox2">
					<button class="underbutton">4</button>
				</view>
			</view>
		</view> -->
		
	</view></view>
</template>

<script>
	export default {
		data() {
			return {
				page:1
			}
		},
		onLoad() {

		},
		methods: {
			jump1(){
				uni.navigateTo({
					url:'/pages/list'
				})
			},
			jump2(){
				uni.navigateTo({
					url:'/pages/chouka'
				})
			},
			jump3(){
				uni.navigateTo({
					url:'/pages/master'
				})
			},
		change(pageid){
			this.page=pageid;
			},
			fanhui(){
				uni.navigateTo({
					url:'/pages/index'
				})
			}
			
		}
	}
</script>

<style>
	.zuoshang {
		position: fixed;
		margin-top: 36rpx;
		margin-left: 15rpx;
	}
	.icon {
		height: 4vh;
		width: 4vh;
		display: flex;
		justify-content: flex-start;
	}
	*{
		margin-right: 1vw;
	}
	.top{
		display: flex;
		flex-direction: column;
		align-items: center;
		
		width: 100vw;
		height:8vh;
		z-index: -2;
		 background: linear-gradient(to   right,#FF6E53 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
	}
	.backcolor{
		
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		width: 100vw;
		height:100vh;
		background-image: linear-gradient(to left , #FFE7AC, #FFBF90);
		margin-top: 15vw;
		
		border-radius: 5% 100% 0 100%;
		
	}
	.topbutton{
		background-color:#f8f3d4;
		color:#393232;
		border-radius: 15px;
		border: none;
		box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
		z-index: 999;
	}
.bigbox
{
	
	
	background-color:#F5F5F5;
	width: 100vw;
	height: 110vh;
	
	z-index: -2;
	
	
}
.middlebox1
{
	margin-left:  2vw ;
	width: 94vw;
	height: 4vh;
	border: 1px;
	border-style: solid;
	border-color: #808080;
	display:flex;
	border-radius: 4px;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
}
.middlebox2
{
	margin-left:  2vw ;
	width: 94vw;
	height: 11vh;
	border: 1px;
	border-style: solid;
	border-color: #808080;
	margin-top: 4vw;
	display: flex;
	justify-content: center;
	align-items: center;
	border-radius: 4px;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
}
.smallbox
{
	margin: 1vw;
	width: 34vw;
	/* border-radius: 8px; */
}
.back
{
	border-style: solid;
	border-color: #808080;
	width: 6vw;
}
.middlebox3
{
	margin-left:  2vw ;
	margin-top: 5vw;
	padding: 1vw;
	border: 1px;
	border-style: solid;
	border-color: #808080;
	width: 93vw;
	height: 45vh;
	border-radius: 4px;
	background-color: #F5F5F5;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.3);
	
}
.middlebox4{
	margin-left:  2vw ;
	margin-top: 5vw;
	display: flex;
	border: 1px;
	border-style: solid;
	border-color: #808080;
	width: 94vw;
	height: 10vh;
	border-radius: 4px;
	display: flex;
	justify-content: center;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.1);
	
	
}

.middlebox5{
	margin-left:  2vw ;
	margin-top: 4vw;
	display: flex;
	justify-content: space-around;
	align-items: center;
	border: 1px;
	border-style: solid;
	border-color: #808080;
	width: 94vw;
	height: 7vh;
	border-radius: 4px;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.1);
	
}

.image{
	height: 8vh;
	width: 15vw;
	border: 1px;
	border-style: solid;
	border-color: #808080;
	margin-top: 2vw;
	margin-left: 3vw;
	margin-right: 3vw;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.1);
}

.underbutton{
	/* margin-right: 3vw; */
	margin-top:2vw;
	height: 5vh;
	width: 20vw;
	background-color:#f8f3d4;
	color:#393232;
	border-radius: 15px;
	border: none;
	box-shadow: 0 0 20px 3px rgba(0, 0, 0, 0.2);
	z-index: 999;
	
	
}
.smallbox2{
	width: 20vw;
	height: 7vh;
	
	
}
	
</style>
