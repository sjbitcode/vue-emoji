import Emoji from './components/Emoji.vue';
import About from './components/About.vue';
import Api from './components/Api.vue';
import Contact from './components/Contact.vue';

export default [
	{
		path: '/',
		component: Emoji
	},

	{
		path: '/about',
		component: About
	},

	{
		path: '/api',
		component: Api
	},

	{
		path: '/contact',
		component: Contact
	}

]