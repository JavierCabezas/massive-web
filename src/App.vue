<template>

  <top></top>

</template>

<script>
  import Top from './components/top/Top.vue'

  export default {
      name: 'app',
      data () {
        return {
          msg: 'Welcome to Your Vue.js App'
        }
      },
      components:{
          'top': Top
      }
  }
</script>