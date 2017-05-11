<template>
    <header class="header">
        <search-bar></search-bar>
        <top-bar></top-bar>
        <nav-bar></nav-bar>
    </header>
</template>

<script>
    import Navbar from './NavBar.vue'
    import TopBar from './TopBar.vue'
    import SearchBar from './SearchBar.vue'

    export default {
        components:{
            navBar: Navbar,
            topBar: TopBar,
            searchBar: SearchBar
        }
    }
</script>