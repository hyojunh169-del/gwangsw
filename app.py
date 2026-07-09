<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>뚱냥이 키우기 극악 버전</title>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <style>
        /* * [CSS 스타일 및 레이아웃]
         * 고등학생 타겟에 맞춘 깔끔하고 트렌디한 카드형 레이아웃 및 뚱냥이 그림 중심 디자인입니다.
         * 브라우저 호환성 오류를 최소화하기 위해 표준 스타일만 사용했습니다.
         */
        body {
            font-family: 'Pretendard', -apple-system, sans-serif;
            background-color: #f0f3f8;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: #333;
        }

        .container {
            width: 100%;
            max-width: 450px;
            background: #ffffff;
            border-radius: 24px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            padding: 24px;
            box-sizing: border-box;
            text-align: center;
        }

        h1 {
            color: #ff6b6b;
            font-size: 26px;
            margin-bottom: 8px;
        }

        .subtitle {
            font-size: 14px;
            color: #666;
            margin-bottom: 20px;
        }

        /* 안내 문구 영역 */
        .info-box {
            background-color: #fff5f5;
            border: 1px solid #ffe3e3;
            border-radius: 16px;
            padding: 14px;
            font-size: 13px;
            text-align: left;
            margin-bottom: 20px;
            line-height: 1.6;
        }
        .info-box ul {
            margin: 6px 0 0 0;
            padding-left: 20px;
        }
        .danger-text {
            color: #e63946;
            font-weight: bold;
        }

        /* 입력 폼 스타일 */
        .input-group {
            margin-bottom: 20px;
            text-align: left;
        }
        .input-group label {
            display: block;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 8px;
        }
        .input-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 16px;
            box-sizing: border-box;
            outline: none;
            transition: border-color 0.2s;
        }
        .input-group input:focus {
            border-color: #ff6b6b;
        }
        .error-msg {
            color: #e63946;
            font-size: 12px;
            margin-top: 6px;
            display: none;
        }

        /* 메인 버튼 스타일 (둥근 버튼) */
        .btn-main {
            background-color: #ff6b6b;
            color: white;
            border: none;
            padding: 14px 28px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 30px;
            cursor: pointer;
            width: 100%;
            box-shadow: 0 4px 10px rgba(255,107,107,0.3);
            transition: all 0.2s;
        }
        .btn-main:hover {
            background-color: #ee5252;
            transform: translateY(-2px);
        }

        /* 상태 배지 */
        .badge-container {
            display: flex;
            justify-content: center;
            gap: 8px;
            margin-bottom: 16px;
        }
        .badge {
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: bold;
            color: white;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        }
        .badge-name { background-color: #4da3ff; }
        .badge-weight { background-color: #ffa04d; }

        /* 뚱냥이 이미지 중심 컨테이너 */
        .cat-container {
            background: #f8f9fa;
            border-radius: 20px;
            padding: 40px 10px;
            margin-bottom: 20px;
            min-height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        .cat-wrapper {
            transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: inline-block;
        }
        /* CSS로 구현한 유연하게 커지는 뚱냥이 그림 전체 */
        .cat-graphic {
            width: 80px;
            height: 75px;
            background-color: #fab1a0;
            border-radius: 50% 50% 45% 45%;
            position: relative;
            margin: 0 auto;
            border: 3px solid #2d3436;
            transition: background-color 0.5s;
        }
        .cat-graphic::before, .cat-graphic::after { /* 귀 */
            content: '';
            position: absolute;
            top: -10px;
            width: 0;
            height: 0;
            border-left: 12px solid transparent;
            border-right: 12px solid transparent;
            border-bottom: 16px solid #fab1a0;
        }
        .cat-graphic::before { left: 6px; transform: rotate(-15deg); }
        .cat-graphic::after { right: 6px; transform: rotate(15deg); }
        
        .cat-face {
            position: absolute;
            top: 25px;
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 16px;
        }
        .cat-eye {
            width: 6px;
            height: 6px;
            background: #2d3436;
            border-radius: 50%;
        }
        .cat-mouth {
            position: absolute;
            top: 33px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            text-align: center;
            font-size: 10px;
            font-weight: bold;
            color: #2d3436;
            line-height: 1;
        }

        /* 게임 조건 동그란 버튼 그룹 */
        .action-group {
            display: flex;
            justify-content: space-around;
            gap: 10px;
            margin-bottom: 25px;
        }
        .btn-circle {
            width: 85px;
            height: 85px;
            border-radius: 50%;
            border: none;
            color: white;
            font-weight: bold;
            font-size: 13px;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: all 0.2s;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 4px;
        }
        .btn-circle:hover { transform: scale(1.08); }
        .btn-food { background: #ff9f43; }
        .btn-water { background: #54a0ff; }
        .btn-treat { background: #ee5253; }

        /* 결과 기록 하이라이트 영역 */
        .result-section {
            border-top: 1px dashed #e0e0e0;
            padding-top: 15px;
            text-align: left;
        }
        .result-title {
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #555;
        }
        .history-list {
            list-style: none;
            padding: 0;
            margin: 0;
            max-height: 120px;
            overflow-y: auto;
            font-size: 13px;
        }
        .history-item {
            padding: 6px 8px;
            border-radius: 6px;
            background: #f8f9fa;
            margin-bottom: 5px;
            display: flex;
            justify-content: space-between;
        }
        .highlight { color: #ee5253; font-weight: bold; }

        /* 화면 전환용 클래스 */
        .hidden { display: none !important; }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1 id="main-title">🐱 뚱냥이 키우기</h1>
            <p class="subtitle">최고의 뚱보 고양이로 진화시켜 보세요!</p>
        </header>

        <div id="screen-input">
            <div class="info-box">
                <strong>💡 핵심 규칙 및 안내 조건</strong>
                <ul>
                    <li>동그란 3가지 버튼(사료, 물, 특식)으로 육성합니다.</li>
                    <li>버튼을 누를 때마다 뚱냥이가 눈에 띄게 커집니다.</li>
                    <li>몸무게 <span class="danger-text">1t (1,000kg)</span> 돌파 시 <strong>'강승우'</strong>로 진화!</li>
                    <li>⚠️ <span class="danger-text">주의:</span> 한 가지 행동만 계속 고집하면 돌연사합니다!</li>
                </ul>
            </div>

            <div class="input-group">
                <label for="username">고양이의 초기 이름을 정해주세요</label>
                <input type="text" id="username" placeholder="예: 나비, 키티, 삼색이" autocomplete="off">
                <div id="error-message" class="error-msg">고양이 이름을 한 글자 이상 입력해 주세요!</div>
            </div>

            <button class="btn-main" onclick="initApp()">키우기 시작 🚀</button>
        </div>

        <div id="screen-game" class="hidden">
            <div class="badge-container">
                <span class="badge badge-name" id="display-name">이름: -</span>
                <span class="badge badge-weight" id="display-weight">3.0 kg</span>
            </div>

            <div class="cat-container">
                <div class="cat-wrapper" id="cat-wrapper">
                    <div class="cat-graphic" id="cat-mesh">
                        <div class="cat-face">
                            <div class="cat-eye" id="eye-l"></div>
                            <div class="cat-eye" id="eye-r"></div>
                        </div>
                        <div class="cat-mouth" id="cat-mouth-text">3__3</div>
                    </div>
                </div>
            </div>

            <div class="action-group" id="action-board">
                <button class="btn-circle btn-food" onclick="feed('food')">🍪<span>사료 주기</span></button>
                <button class="btn-circle btn-water" onclick="feed('water')">💧<span>물 주기</span></button>
                <button class="btn-circle btn-treat" onclick="feed('treat')">🍗<span>특식 주기</span></button>
            </div>

            <button class="btn-main hidden" id="btn-restart" onclick="resetGame()">다시 키우기 🔄</button>

            <div class="result-section">
                <div class="result-title">실시간 육성 피드백 & 기록</div>
                <ul class="history-list" id="history-log"></ul>
            </div>
        </div>
    </div>

    <script>
        /* * [JavaScript 핵심 로직]
         * 예외 및 변수 선언 방식 오류를 방지하기 위해 엄격하게 검증된 로직 구조입니다.
         */
        var currentName = "";
        var weight = 3.0; 
        var scaleValue = 1.0; 
        
        var lastAction = "";
        var sameActionCount = 0;
        var isGameOver = false;

        // 초기 시작 검증 및 셋업
        function initApp() {
            var inputField = document.getElementById('username');
            var errorElement = document.getElementById('error-message');
            
            if (!inputField || !inputField.value.trim()) {
                if (errorElement) errorElement.style.display = 'block';
                return;
            }
            
            if (errorElement) errorElement.style.display = 'none';
            currentName = inputField.value.trim();
            
            // 화면 전환
            document.getElementById('screen-input').classList.add('hidden');
            document.getElementById('screen-game').classList.remove('hidden');
            
            updateUI();
            logHistory(currentName + "(이)가 집사님을 만나서 성장을 시작했습니다!");
        }

        // 핵심 상호작용 기능
        function feed(actionType) {
            if (isGameOver) return;

            // 돌연사 스택 조건 계산
            if (lastAction === actionType) {
                sameActionCount++;
            } else {
                sameActionCount = 1;
                lastAction = actionType;
            }

            if (sameActionCount >= 4) {
                triggerGameOver();
                return;
            }

            // 조건별 증가치 분기
            var gain = 0;
            var actionName = "";
            if (actionType === 'food') { gain = 35.0; actionName = "🍪 사료 주기"; }
            if (actionType === 'water') { gain = 15.0; actionName = "💧 물 주기"; }
            if (actionType === 'treat') { gain = 95.0; actionName = "🍗 특식 주기"; }

            weight += gain;
            
            // 뚱뚱해지는 스케일 시각화 공식 적용
            scaleValue += (gain * 0.015);
            if (scaleValue > 3.5) scaleValue = 3.5; 

            // 1톤 진화 조건 도달 체크
            if (weight >= 1000 && currentName !== "강승우") {
                currentName = "강승우";
                triggerEvolution();
            }

            updateUI();
            logHistory(actionName + " 성공! 몸무게 <span class='highlight'>+" + gain + "kg</span> 증가");
        }

        // UI 갱신 반영
        function updateUI() {
            document.getElementById('display-name').innerText = "이름: " + currentName;
            
            if (weight >= 1000) {
                document.getElementById('display-weight').innerText = (weight/1000).toFixed(2) + " t";
            } else {
                document.getElementById('display-weight').innerText = weight.toFixed(1) + " kg";
            }

            // 그래픽 크기 변환 적용
            document.getElementById('cat-wrapper').style.transform = "scale(" + scaleValue + ")";
        }

        // 히스토리 내역 누적 및 화면 표시
        function logHistory(message) {
            var logBox = document.getElementById('history-log');
            if (!logBox) return;
            var li = document.createElement('li');
            li.className = 'history-item';
            li.innerHTML = "<span>" + message + "</span>";
            logBox.insertBefore(li, logBox.firstChild);
        }

        // 1톤 이상 진화 및 축하 연출
        function triggerEvolution() {
            document.getElementById('main-title').innerText = "👑 초진화 완료";
            document.getElementById('cat-mesh').style.backgroundColor = "#ff7675";
            logHistory("🎊 축하합니다! 뚱냥이가 1t을 돌파하여 최고 존엄 [강승우](으)로 대진화했습니다!");
            
            // 폭죽 효과 안전 실행 조건문
            if (typeof confetti === 'function') {
                confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 } });
            }
        }

        // 돌연사 조건 충족 시 게임 오버
        function triggerGameOver() {
            isGameOver = true;
            document.getElementById('cat-mesh').style.backgroundColor = "#747d8c";
            
            var eyeL = document.getElementById('eye-l');
            var eyeR = document.getElementById('eye-r');
            if (eyeL) { eyeL.style.background = "none"; eyeL.innerText = "x"; }
            if (eyeR) { eyeR.style.background = "none"; eyeR.innerText = "x"; }
            
            var mouthText = document.getElementById('cat-mouth-text');
            if (mouthText) mouthText.innerText = "✖_✖";
            
            logHistory("💀 윽! 같은 행동을 너무 많이 반복하여 고양이가 돌연사했습니다... (게임 실패)");
            document.getElementById('action-board').classList.add('hidden');
            document.getElementById('btn-restart').classList.remove('hidden');
        }

        // 시스템 재설정
        function resetGame() {
            currentName = "";
            weight = 3.0;
            scaleValue = 1.0;
            lastAction = "";
            sameActionCount = 0;
            isGameOver = false;

            document.getElementById('main-title').innerText = "🐱 뚱냥이 키우기";
            document.getElementById('cat-mesh').style.backgroundColor = "#fab1a0";
            
            var eyeL = document.getElementById('eye-l');
            var eyeR = document.getElementById('eye-r');
            if (eyeL) { eyeL.style.background = "#2d3436"; eyeL.innerText = ""; }
            if (eyeR) { eyeR.style.background = "#2d3436"; eyeR.innerText = ""; }
            
            var mouthText = document.getElementById('cat-mouth-text');
            if (mouthText) mouthText.innerText = "3__3";
            
            document.getElementById('username').value = "";
            document.getElementById('history-log').innerHTML = "";

            document.getElementById('action-board').classList.remove('hidden');
            document.getElementById('btn-restart').classList.add('hidden');
            document.getElementById('screen-game').classList.add('hidden');
            document.getElementById('screen-input').classList.remove('hidden');
        }
    </script>
</body>
</html>
