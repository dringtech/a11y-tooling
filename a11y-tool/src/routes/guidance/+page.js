import wcag22 from '../../../../wcag-scraper/wcag22.json';

/** @type {import('./$types').PageLoad} */
export async function load({ params }) {
	return {
		spec: {
			wcag22
		}
	};
}
