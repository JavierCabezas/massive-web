<template>
    <header class="header">
        <top-bar></top-bar>
        <nav-bar></nav-bar>
    </header>
</template>

<script>
    import Navbar from './NavBar.vue'
    import TopBar from './TopBar.vue'

    export default {
        components:{
            navBar: Navbar,
            topBar: TopBar
        }
    }
</script>