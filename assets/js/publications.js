/* MY */
async function loadPublications() {
    try {
        // JSONファイルから論文データを読み込む
        const response = await fetch('publications.json');
        const data = await response.json();
        
        const publicationsList = document.getElementById('publications-list');
        
        data.publications.forEach(pub => {
            // 表示用のHTML要素を作成
            const pubDiv = document.createElement('div');
            pubDiv.className = 'publication';
            
            // 論文情報の表示
            pubDiv.innerHTML = `
                <h2>${pub.title}</h2>
                <p>${pub.authors.join(', ')}</p>
                <p>${pub.journal}, ${pub.volume}(${pub.issue}), ${pub.pages}, ${pub.year}</p>
                <p>DOI: <a href="https://doi.org/${pub.doi}">${pub.doi}</a></p>
            `;
            
            // Zotero用のCOinSメタデータを作成
            const coinSpan = document.createElement('span');
            coinSpan.className = 'Z3988';
            coinSpan.title = `ctx_ver=Z39.88-2004
                &rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal
                &rft.genre=article
                &rft.atitle=${encodeURIComponent(pub.title)}
                &rft.jtitle=${encodeURIComponent(pub.journal)}
                &rft.volume=${pub.volume}
                &rft.issue=${pub.issue}
                &rft.pages=${pub.pages}
                &rft.date=${pub.year}
                &rft.doi=${pub.doi}
                ${pub.authors.map(author => `&rft.au=${encodeURIComponent(author)}`).join('')}
            `.replace(/\s+/g, '');
            
            pubDiv.appendChild(coinSpan);
            publicationsList.appendChild(pubDiv);
        });
        
    } catch (error) {
        console.error('論文データの読み込みに失敗しました:', error);
    }
}

// ページ読み込み時に実行
document.addEventListener('DOMContentLoaded', loadPublications);