<template>
    <audio controls v-if="track !== null">
        <source :src="track" type="audio/mpeg">
    </audio>
</template>

<script>
    export default {
        props: {
            'track': { default: null}
        }
    }
</script>