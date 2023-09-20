<template>
	<view class="bigbox">
		<view class="top">
		</view>
		
		<view class="background">
			<view class="title">
				用户名什么的 大概 我就留个空
			</view>
			<view class="middlebox1">
				<view class="smallbox">
					<button class="button1">
						骆驼信息
					</button>
				</view>
				<view class="smallbox">
					<button class="button1">2</button>
				</view>
				<view class="smallbox">
					<button class="button1">3</button>
				</view>
			
				
			</view>
			
			
			
		</view>
		<view class="middlebox2">
			<form class="form1" action="">
				<view class="formtitle">
					骆驼名字
				</view>
				
				<input type="text" class="text" name="name"  placeholder="请输入名字"/>
				<view class="formtitle">
					年龄
				</view>
				<input type="text" class="text" name="name"  placeholder="请输入年龄"/>
				<view class="form">
					<view class="formtitle">
					骆驼体型
					</view>
					
					<label class="radio">
						<radio for="pang" value="body1" name="body"  checked="body === '1'" @click="handleRadioClick(1)"/><text id="pang">胖</text>
					</label>
					<label class="radio1">
						<radio for="weipang" value="body2" name="body" checked="body === '2'" @click="handleRadioClick(2)" /><text id="weipang" >微胖</text>
					</label>
					<label class="radio1">
						<radio for="shou" value="body3" name="body"/><text id="shou">瘦</text>
					</label>
					<label class="radio1">
						<radio for="henshou" value="body4" name="body"/><text id="henshou">很瘦</text>
					</label>   
					  
					
					  
				</view>
			</form>
			
			
			
			
			
			
			<form class="form2" action=""></form>
		</view>
		<view class="middlebox3">
			<view class="smallbox2">
				<button class="bottombutton">1</button>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				 body: '',
				
			};
		},
		methods: {
			 handleRadioClick(value) {
			      this.body = value.toString();}
		}
	}
</script>

<style>
	
.bigbox{
	display: flex;
	flex-direction: column;
	align-items: center;
}
.top{
	width: 100vw;
	height:6vh;
	z-index: -1;
	 background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
}
.background{
	background: linear-gradient(to   right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
	width: 100vw;
	height: 30vh;
	z-index: -2;
	padding-top: 2vw;
	display: flex;
	flex-direction: column;
	align-items: center;
	/* margin-top: 6vh; */
}
.title{
	font-size: 2vh;
	font-weight: bold;
	align-self: flex-start;
	text-indent: 2em;
	color: #fff1cf;
	
	
	
}
.middlebox1{
	display: flex;
	justify-content: space-around;
	width: 94vw;
	height: 5vh;
	margin-top: 13vw;
	
}
.smallbox{
	
	
	width: 25vw;
	height: 6vh;
	margin-bottom: 10vw;
}
.button1{
	height: 5vh;
	text-align: center;
	border-radius: 10vw;
	background-color:#f8f4e6;
	color:#494a41;
	border-radius: 5px;
	border: none;
	box-shadow: 0 0 35px 2px rgba(0, 0, 0, 0.2);
	font-size: 1rem;
	
	
}
.middlebox2
{
	width: 84vw;
	height: 60vh;
	
	margin-top: -25vw;
	border-radius: 40px;
	border: none;
	box-shadow: 0 0 50px 3px rgba(0, 0, 0, 0.2);
	background-color: #F5F5F5;
	display: flex;
	flex-direction: column;
	padding: 2vw;
	align-items: center;
	
	
}
.formtitle{
	/* text-indent: 1em; */
	color: #808080;
	margin-top: 4vw;
	font-size: 1rem;
	margin-bottom: 1vw;
	
}
.text{
	width: 66vw;
	height: 3vh;
	
	border-width: 1px;
	
	
	border-bottom:solid 1px #BEBDBF;
	margin-top: 1vw;
	/* margin: 1vw; */	
}
.form{
	margin-top: 2vw;
}
.radio1{
	margin-left: 5vw;
	
}
.middlebox3{
	margin-top: 7vw;
	width: 100vw;
	height: 10vh;
}
.smallbox2{
	width: 100vw;
	height: 15vh;
}
.bottombutton{
	width: 90vw;
	text-align: center;
	border-radius:  15px;
	background: linear-gradient(to  bottom right,#FF6E53 0 , #FF6E52 , #FF8453  , #FF9758  ,#FFA859 100% );
	color:#393232;
	border: none;
	box-shadow: 0 0px 29px 1px rgba(0, 0, 0, 0.2);
	color: #fff1cf;
}
text::-moz-placeholder {
	  color:  red;
	}
</style>
