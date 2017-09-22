<template>
    <div>
        <ul>
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
            <li><a href="#">Link 3</a></li>
            <li class="current"><a href="#">Link actual</a></li>
        </ul>
    </div>
</template>

<style>
    ul {
        list-style-type: none;
    }
    ul li {
        float: left;
        padding: 10px;
        width: auto;
        color: #B67E90;
    }
    ul li::after {
        content: ">";
        padding-left: 10px;
        color: #000;
    }
    ul li.current {
        color: #6E5C7A;
        font-weight: bold;
    }

    ul li.current::after {
        content: none;
    }
</style>