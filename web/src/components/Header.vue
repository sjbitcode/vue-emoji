<template>
    <section class="hero is-primary is-bold">
        <div class="hero-body">
            <div class="container has-text-centered">
                <h1 class="title">
                    &#x1F649; Emoji Index &#x1F64A;
                </h1>
                <h2 class="subtitle">
                    search &amp; filter emoji
                </h2>
                <div>
                    <b-tabs type="is-toggle-rounded" position="is-centered" class="block">
                        <b-tab-item label="home"></b-tab-item>
                        <b-tab-item label="about"></b-tab-item>
                        <b-tab-item label="api"></b-tab-item>
                        <b-tab-item label="contact"></b-tab-item>
                    </b-tabs>
                </div>
            </div>
        </div>
    </section>
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