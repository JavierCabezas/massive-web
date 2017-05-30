<template>
  <div>
    <top></top>
    <transition name="fade">
      <router-view></router-view>
    </transition>
    <bottom></bottom>
  </div>
</template>

<script>
  import Top from './components/top/Top.vue'
  import Home from './components/main/Home.vue'
  import Bottom from './components/footer/Bottom.vue'

  export default {
      name: 'app',
      data () {
        return {
          msg: 'Welcome to Your Vue.js App'
        }
      },
      created: function () {
          this.$translate.setLang('en_US');
      },
      components:{
          top: Top,
          home: Home,
          bottom: Bottom
      }
  }
</script>