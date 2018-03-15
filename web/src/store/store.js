import Vue from 'vue';
import Vuex from 'vuex';
import _ from 'lodash';

Vue.use(Vuex);

export const store = new Vuex.Store({
	state: {
		title: 'Emoji Index',
		
		api_status: '\ud83e\udd1e\ud83c\udffc',
		thumbsUp: '\ud83d\udc4d\ud83c\udffc',
		thumbsDown: '\ud83d\udc4e\ud83c\udffc',

		baseUrl: 'http://localhost:8000',
		emojiEndpoint: '/emoji',
		categoriesEndpoint: '/categories',
		statsEndpoint: '/stats',
		homepageEndpoint: '/homepage?flat=true',
		sampleRequestQueryParams: '?q=smile&limit=2',

		homepageEmoji: [],
		categories: {},
		sampleRequest: {},
		stats: {
			'date_requested': '',
			'Total Emojis': 0,
			'Total Keywords': 0,
			'Recently Added Emojis': 0,
			'Total Main Categories': 0,
			'Total Sub Categories': 0
		}
	},

	getters: {
		homepageUrl: state => {
			return state.baseUrl + state.homepageEndpoint;
		},

		categoriesUrl: state => {
			return state.baseUrl + state.categoriesEndpoint;
		},

		statsUrl: state => {
			return state.baseUrl + state.statsEndpoint;
		},

		sampleRequestUrl: state => {
			return state.baseUrl + state.emojiEndpoint + state.sampleRequestQueryParams;
		}
	},

	mutations: {
		updateMessage: (state, payload) => {
			if (payload === 'good') {
				state.api_status = state.thumbsUp;
			}
			else if (payload === 'bad') {
				state.api_status = state.thumbsDown;
			}
		},

		updateHomepageEmoji: (state, payload) => {
			state.homepageEmoji = payload;
		},

		updateCategories: (state, payload) => {
			state.categories = payload;
		},

		updateStats: (state, payload) => {
			state.stats = payload;
		},

		updateSampleEmojiRequest: (state, payload) => {
			state.sampleRequest = payload;
		}
	},

	actions: {
		fetchMessage: context => {
			if(! context.state.message) {

				const url = context.state.baseUrl;

				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateMessage', 'good');
				})
				.catch(error => {
					context.commit('updateMessage', 'bad');
					console.log('Error fetching data, ' + error);
				});
			}
		},

		fetchHomepageEmoji: context => {
			if(_.isEmpty(context.state.homepageEmoji)) {

				const url = context.getters.homepageUrl;

				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateHomepageEmoji', data.results);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
		},

		fetchCategories: context => {
			if(_.isEmpty(context.state.categories)) {
				
				const url = context.getters.categoriesUrl;

				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateCategories', data.results);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
		},

		fetchStats: context => {
			if(context.state.stats['Total Emojis'] === 0) {
				
				const url = context.getters.statsUrl;

				Vue.http.get(url)
				.then(data => {
					return data.json();
				})
				.then(data => {
					context.commit('updateStats', data);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
		},

		fetchSampleEmojiRequest: context => {
			if(_.isEmpty(context.state.sampleRequest)) {
	
				const url = context.getters.sampleRequestUrl;
	
				Vue.http.get(url)
				.then(data => {
					return data.json()
				})
				.then(data => {
					context.commit('updateSampleEmojiRequest', data);
				})
				.catch(error => {
					console.log('Error fetching data, ' + error);
				});
			}
		}
	}
})