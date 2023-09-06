function readText(url){
	var _resolve;
	// 调用 `fetch()`，传入 URL。
	fetch(url)
	  // fetch() 返回一个 promise。当我们从服务器收到响应时，
	  // 会使用该响应调用 promise 的 `then()` 处理器。
	  .then((response) => {
	    // 如果请求没有成功，我们的处理器会抛出错误。
	    if (!response.ok) {
	      throw new Error(`HTTP 错误：${response.status}`);
	    }
	    // 否则（如果请求成功），我们的处理器通过调用
	    // response.text() 以获取文本形式的响应，
	    // 并立即返回 `response.text()` 返回的 promise。
	    return response.text();
	  })
	  // 若成功调用 response.text()，会使用返回的文本来调用 `then()` 处理器，
	  // 然后我们将其拷贝到 `poemDisplay` 框中。
	  .then((text) => (_resolve(text)))
	  // 捕获可能出现的任何错误，
	  // 并在 `poemDisplay` 框中显示一条消息。
	  .catch((error) => (console.log(error)));
	  return new Promise((resolve)=>(_resolve = resolve));
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
	var frag;
	var _resolve;
	readText(path).then((text)=>{
		frag = parseNodeText(text, className);
		console.log(frag);
		_resolve(frag);
	});
	return new Promise((resolve)=>{
		_resolve = resolve;
	});
}
function getFilesByIndexString(str){
	var strArray = new Array();
	var s = "";
	var idx = 0;

	while(idx < str.length){
		let ch = str.charAt(idx);
		if(ch == "\r" || ch == "\n")
		continue;
		while(idx < str.length){
			s = s + str.charAt(idx);
			++idx;
		}
		strArray.push(s);
		s = "";
	}

}
function foreachFileInIndexFile(path){
	var _resolve;
	readText(path).then((text)=>{console.log(text);getFilesByIndex(text).forEach((e)=>{_resolve(e)})});
	return new Promise((resolve)=>{
		_resolve = resolve;
	});
}
foreachFileInIndexFile("test/a.txt").then((str)=>{console.log(str); return getPassageFrag(str)}).then((frag)=>{document.body.appendChild(frag)});
//getPassageFrag("scripts/test.txt", "paragraph").then((frag)=>{document.body.appendChild(frag)});