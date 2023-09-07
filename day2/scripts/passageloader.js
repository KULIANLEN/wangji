"use strict"
function readText(url){
	return fetch(url)
	  .then((response) => {
	    if (!response.ok) {
	      throw new Error(`HTTP 错误：${response.status}`);
	    }
	    return response.text();
	  });
}
function parseNodeText(text, className = null){
	let frag = document.createRange().createContextualFragment(text);
	if(className != null){
		frag.childNodes.forEach((node)=>{
			node.className = className;
		});
	}
	return frag;
}
function getPassageFrag(path, className = null){
	return readText(path).then((text)=>{
		return new Promise((resolve)=>{
			resolve(parseNodeText(text, className));
		});
	});
}
function getFilesByIndexString(indexStr){
	var indexes = indexStr.match(/.+/g);
	for(let i = 0; i < indexes.length; ++i){
		var elemArray = indexes[i].match(/[^\t]+/g);
		indexes[i] = {title: elemArray[0], date: elemArray[1], path: elemArray[2]};
	}
	return indexes;
}
function filesInIndexFile(path){
	return readText(path).
	then((text)=>{
		return new Promise((resolve)=>{
			resolve(getFilesByIndexString(text));
		})
	});
}
