<template>
  <div class="invite-container">
    <div v-if="showInviteCode" class="animate__animated animate__fadeIn">
      <div class="invite-card">
        <h2 class="invite-title">邀请码</h2>
        <h3 class="invite-code">{{ inviteCode }}</h3>
        <p class="invite-description">使用此邀请码注册以获得特殊奖励！</p>
        <button class="copy-button" @click="copyInviteCode">复制</button>
      </div>
      <button class="back-button" @click="goBack">返回</button>
    </div>
    <div v-else class="animate__animated animate__fadeIn">
      <div class="input-container">
        <input type="text" v-model="inputInviteCode" placeholder="请输入邀请码" class="invite-input-field">
        <button class="submit-button" @click="submitInviteCode">提交</button>
      </div>
      <button class="generate-button" @click="generateInviteCode">生成邀请码</button>
    </div>
  </div>
</template>

<style scoped>
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
  padding: 4px 8px;
  margin-top: 8px;
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

.copy-button:hover,
.submit-button:hover,
.generate-button:hover,
.back-button:hover {
  background-color: #f44336;
}

.invite-input-field {
  padding: 8px;
  border: none;
  border-radius: 4px;
  width: 200px;
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
  margin-left: 4px;
}

.generate-button {
  margin-top: 8px;
  padding: 8px 16px;
  font-size: 12px;
}

.back-button {
  margin-top: 8px;
  padding: 8px 16px;
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
      showInviteCode: false
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
      const textarea = document.createElement("textarea");
      textarea.value = this.inviteCode;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand("copy");
      document.body.removeChild(textarea);
      alert("邀请码已复制到剪贴板");
    },
    goBack() {
      this.showInviteCode = false;
    }
  }
};
</script>