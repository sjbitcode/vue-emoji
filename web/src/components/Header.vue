<template>
    <header>
        <section class="hero is-primary is-bold">
            <div class="hero-body">
                <div class="container has-text-centered">
                    <h1 class="title">
                        &#x1F649; Emoji Index &#x1F64A;
                    </h1>
                    <h2 class="subtitle">
                        search &amp; filter emoji
                    </h2>
                    <div style="display: inline-block;">
                        <p v-on:click="show_about = !show_about">
                            <a>about</a>
                        </p>
                        <p>
                            <a>api</a>
                        </p>
                        <p>
                            <a>contact</a>
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <app-about v-show="show_about"></app-about>
    </header>
</template>


<script>
    import About from './About.vue';

    export default {
        props: {
            title: {
                type: String,
                required: true
            }
        },

        components: {
            'app-about': About
        },

        data() {
            return {
                show_about: false
            }
        }
    }
</script>


<style scoped>
a {
    color: #ab9bdc;
}
</style>