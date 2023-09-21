<template>
  <view class="invite-container ">
    <view v-if="showInviteCode" class="animate__animated animate__fadeIn">
		 
		 <image src="/static/OIP-C_00000.png" class="image2"></image>
      <view class="invite-card">
		 
        <h2 class="invite-title">邀请码</h2>
        <h3 class="invite-code">{{ inviteCode }}</h3>
        <p class="invite-description">使用此邀请码注册以获得特殊奖励！</p>
        <button class="copy-button" @click="copyInviteCode">复制</button>
      </view>
      <button class="back-button" @click="goBack">返回</button>
	  <view class="">
	  	<image src="/static/R-C_00000.png" class="image1"></image>
	  </view>
	  <view>
	  	<!-- <view class='tanchuang' v-if="showtc">
	  		邀请码已复制到剪贴板！
	  	</view> -->
	  </view>
	  
    </view>
	
	
	
    <view v-else class="animate__animated animate__fadeIn  " >
		
		
		<view class="bigbox">
			<view class="background">
				<image src="/static/background_00000.png" class="image"></image>
				<view class="top">
					
				</view>
			</view>
			<view class="bigtitle">
				<text>邀请好友</text>
			</view>
			<view class="bigtitle2">
				<text>邀好友，一起拿证</text>
			</view>
			<view class="middlebox">
				<view class="titlebox">
					<view class="title">
						<text class="wenzi1">您的专属邀请码</text>
					</view>
				</view>
				<view class="logo">
					<image src="/static/cyzx.jpg" class="logo" ></image>
				</view>
				<view class="smallbox">
				   <input type="text" v-model="inputInviteCode" placeholder="               请输入邀请码" class="invite-input-field ">	
				</view>
				<view class="smallbox">
					<button class="submit-button " @click="submitInviteCode">提交</button>
				</view>			
				<view class="smallbox2">
					<button class="generate-button" @click="generateInviteCode">生成邀请码</button>	
				</view>
				
			</view>
			
			
		</view>
			
		
			
      
     </view>
  </view>
</template>

<style scoped>
	.tanchuang{
		height: 100rpx;
		width: 100rpx;
		
	}
	.top{
		position: absolute;
		top: 0%;
		top: 0vh;
		width: 100vw;
		height:6vh;
		background: linear-gradient(to   left,#FF6E53 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
	}
	.background{
		/* margin-top: -4vh; */
		background: linear-gradient(to   left,#FF6E53 , #FF6E52 , #FF8453 40% , #FF9758  ,#FFA859 );
	}
	.image2{
		width: 20vw;
		height: 10vh;
		margin-top: 18vh;
		margin-left: -10vw;
	}
	.image1{
		z-index: -2;
		width:36vw;
		height: 18vh;
		margin-top: -30vh;
		margin-left: 48vw;
		
	}
	.bigtitle2{
		font-size: 60rpx;
		color: #555555;
		
		
	}
	.bigtitle{
		font-size: 90rpx;
		margin-top: -172vw;
	}
	.logo{
		margin-top: -7vw;
		width: 28vw;
		height: 15vh;
		border-radius: 50%;
		
	}
.wenzi1{
	margin-left: 7vw;
}
	.title{
		width: 45vw;
		height: 5vh;
		margin-top: -17vh;
		box-shadow: 1px 2px 1px 1px rgba(0, 0, 0, 0.2);
		background-image: linear-gradient(to right, #f2994a, #ffd200);
		border-radius: 2vw;
		line-height: 5vh;
		
		
	}
	.middlebox{
		display: flex;
		flex-direction: column;
		align-items: center;
		width: 84vw;
		height: 46vh;
		border-style: none;
		border-radius: 7vw;
		padding-top: 15vh;
		box-shadow: 10px 5px 30px 2px rgba(0, 0, 0, 0.2);
		background-color: #eaeaea;
		
	}
	.smallbox2{
		margin-top: 2vh;
	}
	.smallbox{
		margin-top: 3vh;
	}
	.middlebox{
		margin-top: 7vh;
		
	}
	.bigbox{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.image{
		z-index: -5;
		width: 100vw;
		height: 100vh;
	}
	
	
	
.invite-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 30px;
  
}

.invite-card {
  background-color: #f5f5f5;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .2);
  text-align: center;
  margin-top: -6vh;
}

.invite-title {
  font-size: 20px;
  margin: 0;
}

.invite-code {
  font-size: 36px;
  font-weight: bold;
  color: #ff5722;
  margin-bottom: 20px;
}

.invite-description {
  font-size: 14px;
  margin: 0;
  color: #444444;
}

.copy-button,
.submit-button,
.generate-button,
.back-button {
  /* padding: 4px 8px;
  /* margin-top: 8px; */
 width: 50vw;
 height: 5vh;
  background-color: #ff5722;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  outline: none;
  transition: background-color 0.3s;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .2);
}
.copy-button{
	margin-top: 2vw;
}

.back-button{
	margin-top: 5vw;
}

.copy-button:hover,
.submit-button:hover,
.generate-button:hover,
.back-button:hover {
  background-color: #f44336;
}

.invite-input-field {
  /* padding: 8px; */
  margin-top: -7vw;
  height: 5vh;
  border: none;
  border-radius: 4px;
  width: 50vw;
  outline: none;
  font-size: 12px;
  background-color: #f5f5f5;
  color: #444444;
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, .2);
}

.invite-input-field::placeholder {
  color: #999999;
}

.submit-button {
 /* margin-left: 4px; */
}

.generate-button {
  /* margin-top: 8px;
  padding: 8px 16px; */
  font-size: 12px;
}

.back-button {
 /* margin-top: 8px;
  padding: 8px 16px; */
  background-color: #cccccc;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 12px;
  outline: none;
  transition: background-color 0.3s;
}

.back-button:hover {
  background-color: #999999;
}

/* 动画效果 */
.animate__animated {
  animation-duration: 0.5s;
  animation-fill-mode: both;
  width: 70vw;
}

.animate__fadeIn {
  animation-name: fadeIn;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>

<script>
export default {
  data() {
    return {
      inviteCode: "",
      inputInviteCode: "",
      showInviteCode: false,
	  showtc:false
    };
  },
  methods: {
    generateInviteCode() {
      this.inviteCode = this.generateRandomString(8);
      this.showInviteCode = true;
    },
    generateRandomString(length) {
      const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
      let result = "";
      for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        result += characters.charAt(randomIndex);
      }
      return result;
    },
    submitInviteCode() {
      console.log("输入的邀请码", this.inputInviteCode);
      this.inputInviteCode = "";
    },
    copyInviteCode() {
		uni.showToast({
		        title: '邀请码已复制！',
		        icon: 'success',
		        duration: 2000,
		        mask: true,
				
		      });
      const textarea = document.createElement("textarea");
      textarea.value = this.inviteCode;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
	  this.showtc=true;
	  setTimeout(() => {
	    this.showtc = false;
	  }, 3000);
    },
    goBack() {
      this.showInviteCode = false;
    }
  }
};
</script>