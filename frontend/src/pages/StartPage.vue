<template>
  <div class="container">
    <div class="flex-container">
      <div class="left-side">
        <div class="discription">
          <h1>KISHIMENとは？</h1>
          工業立国を模索する明治政府が、専門技術の素養を備えた優れた職工長・工業教員の養成を目的に設立した、学制下での最初の工業教育機関である東京職工学校を母体とする。
          現在は、伝統的な理学系、工学系に加え、情報系、バイオ系、社会・経営系をカバーする、理工系総合大学となっている。
          2012年に文部科学省の世界トップレベル国際研究拠点形成促進プログラムによりELSI（東京工業大学地球生命研究所）が発足するなど、各学問領域において研究が進められている。
          2000年にノーベル化学賞を受賞した白川英樹工学博士は卒業生、2016年にノーベル生理学・医学賞を受賞した大隅良典も本大学の教授である。
          理工系が主体だが、人文・社会系においてもリベラルアーツ研究教育院を中心に研究・教育が行われる。長らく教鞭をとった著名な学者に文芸評論家の江藤淳（名誉教授）や社会学者の橋爪大三郎（名誉教授）がいる。哲学者の鶴見俊輔も助教授として数年間在籍していた。池上彰やパトリック・ハーランなどのタレント講師も教鞭をとっている。
          2022年8月に、東京医科歯科大学と統合する方針を公表し[2]、同月9日に同大学と統合に関する協議を開始した[3]。なお、東京医科歯科大学と合併する事によりh5-indexが169となり国内第2位となる。
        </div>
        <button
          class="start-button"
          @mouseover="btnOver"
          @mouseleave="btnLeave"
          @click="goMainpage"
        >
          Lets start!
        </button>
      </div>
      <div class="right-side">
        <img
          src="https://resize2-icotto.k-img.com/RQxND1N0oIB-MMWKyooFxpOYWC3F8fPGoLJVLrpjHSk/rs:fill:1400:934/plain/https://icotto.k-img.com/uploads/press_image/000/09d/87b/image/bc40397be9b6939f256e6655fe46ac64.jpeg"
          alt="きしめん"
          class="image"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const colors = {
  team_color: '#ff971d',
  white: '#ffffff',
  black: '#000000'
}

const router = useRouter()

const btn_color = ref(colors.white)
const btn_txt_color = ref(colors.black)

const btnOver = () => {
  btn_color.value = colors.team_color
  btn_txt_color.value = colors.white
}
const btnLeave = () => {
  btn_color.value = colors.white
  btn_txt_color.value = colors.black
}
const goMainpage = () => {
  router.push('main')
}
</script>

<style lang="scss">
.container {
  width: 100vw;
  height: 100vh;
  /* background-color: red; */
}

.flex-container {
  display: flex;
  justify-content: space-around;
  width: 100%;
  height: 100%;
}

.left-side {
  padding: 5% 0 5% 0;
  width: 45%;
  height: 90%;
  /* background-color: black; */
}
.right-side {
  padding: 5% 0 5% 0;
  width: 45%;
  height: 90%;
  /* background-color: green; */
}

.discription {
  width: 100%;
  height: 50%;
  background-color: white;
}
.image {
  margin-right: 20px;
  margin-top: 100px;
  width: 100%;
  height: 50%;
  /* background-color: black; */
}
.start-button {
  margin-top: 15%;
  width: 100%;
  height: 20%;
  font-size: 50px;
  box-shadow: none;
  border-style: solid;
  border-radius: 30px;
  border-color: #ff971d;
  transition: 0.5s;
  background-color: v-bind(btn_color);
  color: v-bind(btn_txt_color);
}

/* .start-button2 {
  
} */
</style>
