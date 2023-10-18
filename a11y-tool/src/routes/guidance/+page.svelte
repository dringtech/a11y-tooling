<script>
	import WCAGNode from '$lib/WCAGNode.svelte';
	const title = 'WCAG Guidance';

	/** @type {import('./$types').PageData} */
	export let data;
	let level = 'A';
	let inclusive = true;
	let chosenSpec = 'wcag22';
	$: spec = data.spec[chosenSpec];
	$: levelFilter = (c) => {
		const t = c.level?.length;
		if (!t) return false;
		if (inclusive) return t <= level.length;
		return t == level.length;
	};
</script>

<h1>{title}</h1>

<label for="level">Level selected: </label>
<select id="level" bind:value={level}>
	<option value="A">A</option>
	<option value="AA">AA</option>
	<option value="AAA">AAA</option>
</select>
<input id="inclusive" type="checkbox" bind:checked={inclusive} />
<label for="inclusive">Include lower levels</label>

{#each spec.principles as principle}
	<WCAGNode {...principle} level="2">
		{#each principle.guidelines as guideline}
			<WCAGNode {...guideline} level="3">
				{#each guideline.criteria.filter(levelFilter) as criterion}
					<WCAGNode {...criterion} level="4">
						<p><span data-wcag-level={criterion.level}>{criterion.level}</span></p>
					</WCAGNode>
				{/each}
			</WCAGNode>
		{/each}
	</WCAGNode>
{/each}
