<template>
	<view>
	<view class="zuoshang">
			<image src='/static/hhh/jiantou.png' class="icon" @click="fanhui()"></image>
		</view>
  <view class="back">
    <view class="top">
      <view class="jiangquan">
        <img class="jqpic" src="/static/youhuiquan.png" />
        <view class="quantity">12</view>
        <img class="add" @click="addjq" src="/static/add.png" />
      </view>
    </view>
    <view class="card-container">
      <view v-for="(card, index) in cards" :key="index" class="card-slot">
        <view class="card-wrapper" :class="{ 'hidden': card.hidden, 'flipped': card.flipped }">
          <view class="card-front">
            <img :src="card.image" :alt="card.name" />
          </view>
          <view class="card-back">
            <img class="backimg" :src="card.back" :alt="card.name" />
            <span>{{ card.name }}</span>
          </view>
        </view>
      </view>
      <view class="buttons-container">
        <button class="draw-btn" @click="drawCard(1)">单抽</button>
        <button class="draw-btn" @click="drawCard(9)">九连抽</button>
      </view>
    </view>
    <!-- <view class="popup" v-if="showPopup">
      <view class="popup-content">
        <p>我的邀请码：DAS6D4</p>
        <view class="tianxie_yqm">
          <label for="inviteCode">请填写邀请码：</label>
          <input id="inviteCode" class="putyqm" v-model="inviteCode" />
        </view>
        <button @click="submit">提交</button>
        <button @click="showPopup = false">关闭</button>
      </view>
    </view> -->
    <view class="popup2" v-if="showPopup2">
      <view class="popup-content">
        <p>您获得了：</p>
        <view class="get">123</view>
		<button @click="close">关闭</button>
      </view>
    </view> 
	<view class="yinbi" v-if="yinbi"></view>
  </view>
	 
  </view>
</template>

<script>
export default {
  data() {
    return {
      cards: [
        { image: '/static/hhh/2.jpg', name: '1', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '2', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '3', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '4', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '5', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '6', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '7', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '8', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
        { image: '/static/hhh/2.jpg', name: '9', hidden: true, flipped: false, back: '/static/hhh/kabei.jpg' },
      ],
      // showPopup: false,
      showPopup2: false,
	  yinbi:false,
      inviteCode: ''
    };
  },
  methods: {
    drawCard(count) {
	  this.yinbi=true;
      const hiddenCards = this.cards.filter((card) => card.hidden === true);
      const shuffledCards = this.shuffleArray(hiddenCards);
      let index = 0;
      const drawInterval = setInterval(() => {
        if (index >= count || index >= shuffledCards.length) {
          clearInterval(drawInterval);
        } else {
          const card = shuffledCards[index];
          card.hidden = false;
          this.animateCard(card, index * 100);
        }
        index++;
      }, 400);
      let cnt = count * 400;
      cnt += 2000;
      setTimeout(() => {
        this.showPopup2 = true;
		this.yinbi=false;
      }, cnt);
    },
    animateCard(card, delay) {},
    shuffleArray(array) {
      const shuffledArray = [...array];
      for (let i = shuffledArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [shuffledArray[i], shuffledArray[j]] = [shuffledArray[j], shuffledArray[i]];
      }
      return shuffledArray;
    },
    addjq() {
      uni.navigateTo({
      	url:"/pages/yaoqing"
      })
    },
    submit() {},
	close(){
		this.showPopup2=false;
		location.reload();
	},
	fanhui(){
		uni.navigateTo({
			url:'/pages/index'
		})
	}
  }
};
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
	.yinbi{
		position: fixed;
		top: 0;
		left: 0;
		width:100vw;
		height: 100vh;
		background-color: rgba(0,0,0,0);
		z-index:50;
	}
.back {
  background: linear-gradient(to right, #ff6e53 0, #ff6e52, #ff8453, #ff9758, #ffa859 100%);
}

.popup,
.popup2 {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.tianxie_yqm {
  margin-bottom: 20px;
}

.tianxie_yqm label {
  display: block;
  margin-bottom: 10px;
}

.putyqm {
  width: 200px;
  height: 30px;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

.add {
  /* margin-top: -20px; */
  width: 30rpx;
  height: 30rpx;
}

.quantity {
  
}

.jqpic {
  /* margin-top: -20px; */
  width: 50rpx;
  height: 50rpx;
}

.jiangquan {
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-wrap: nowrap;
  border: #000;
  border-style: dotted;
  position: absolute;
  top: 0;
  right: -5vw;
  transform: translate(-50%, 50%);
  padding-top: 2rpx;
  background-color: #c2ccd0;
  width: 150rpx;
  height: 70rpx;
}

.top {
  margin-top: 0;
  width: 100vw;
  height: 9vh;
  z-index: -2;
}

.backimg {
  display: flex;
  width: 220px;
  margin-left: 30px;
}

.card-container {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 20px;
}

.card-slot {
  position: relative;
  width: 100px;
  height: 150px;
  margin: 10px;
  perspective: 800px;
  cursor: pointer;
}

.card-wrapper {
  position: absolute;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.card-wrapper.hidden {
  transform: rotateY(180deg);
}

.card-wrapper.flipped {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 10px;
  overflow: hidden;
  transform: rotateY(0deg);
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.card-front {
  background-color: #f1f1f1;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}



.card-front img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-back {
  transform: rotateY(180deg);
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  font-size: 24px;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}



.buttons-container {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.draw-btn {
  /* margin: 0 10px; */
  margin-left: 30rpx;
  padding: 10px 20px;
  font-size: 16px;
  width: 200rpx;
  height: 100rpx;
 
  color: #f5f5f5;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
  background-image: linear-gradient(to left , #FFE7AC, #FFBF90);
  
}

.draw-btn:hover {
  background-color: #333;
}

.popup2 {
  background-color: rgba(0, 0, 0, 0.8);
}

.popup2 .popup-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

.popup2 .get {
  font-size: 24px;
  font-weight: bold;
  color: #ff6e53;
  margin-top: 10px;
}
</style>