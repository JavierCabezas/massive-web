<template>
  <div>
    <top></top>
    <home></home>
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
      components:{
          top: Top,
          home: Home,
          bottom: Bottom
      }
  }
</script>