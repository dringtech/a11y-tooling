<script>
	export let id;
	export let label;
	export let title;
	export let description;
	export let level = '2';
</script>

<section {id}>
	<svelte:element this={'h' + level}>{label}. {title}</svelte:element>
	<p>{description}</p>
	<slot />
</section>
