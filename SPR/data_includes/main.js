//An example script for self-paced reading experiment (DashedSentenceNoSpace)
//DebugOff()   // Uncomment this line only when you are 100% done designing your experiment

//two different experiments and fillers
//Experiemnt A with 2 conditions (X_a, X_b)
//EXperiment B with 2 conditosns (Y_a, Y_b)
//fillers: "f"

var shuffleSequence = seq("intro",
                          sepWith("sep",
                                  seq("practice",
                                      rshuffle(
                                        anyOf("X_a", "X_b"),
                                        anyOf("Y_a", "Y_b"),
                                        "f")
                                    )
                                  )
                                );

//var shuffleSequence = seq("intro", sepWith("sep", seq("practice", rshuffle("s1", "s2"))), sepWith("sep", rshuffle("q1", "q2")));

var practiceItemTypes = ["practice"];

var defaults = [
    "Separator", {
        transfer: 1000,
        normalMessage: "次の文が出るまでお待ちください",
        errorMessage: "残念、不正解です！"
    },
/*    "DashedSentence", {
        mode: "self-paced reading"
    },*/
    "DashedSentenceNoSpace", {
        mode: "self-paced reading"
    },

    "Question", {
        hasCorrect: true,
        randomOrder: false,
        as: ["はい", "いいえ"],
    },
    "Message", {
        hideProgressBar: true
    },
    "Form", {
        hideProgressBar: true,
        continueOnReturn: true,
        continueMessage: "続けるには、ここをクリックしてください",
        saveReactionTime: true
    },
    "FormCounts", {
        //"html" option is obligatory
        hideProgressBar: false,
        countsForProgressBar: true,
        continueMessage: "続けるには、ここをクリックしてください",
        continueOnReturn: false,
        saveReactionTime: true
    }
];

var showProgressBar = false;//
var progressBarText = "進捗状況";
//var practiceItemTypes = ["practice"];//
//var practiceMessage = "練習";//
var centerItems = true;

var sendingResultsMessage = "結果を送信中です";

//結果送信終了後のコメント//
var completionMessage = "ありがとうございました。これで実験は終了です。お疲れさまでした。";
//結果送信失敗時のコメント//
var completionErrorMessage = "データの送信に失敗しました。お手数ですが担当者までお問い合わせください。";

var items = [

    // New in Ibex 0.3-beta-9. You can now add a '__SendResults__' controller in your shuffle
    // sequence to send results before the experiment has finished. This is NOT intended to allow
    // for incremental sending of results -- you should send results exactly once per experiment.
    // However, it does permit additional messages to be displayed to participants once the
    // experiment itself is over. If you are manually inserting a '__SendResults__' controller into
    // the shuffle sequence, you must set the 'manualSendResults' configuration variable to 'true', since
    // otherwise, results are automatically sent at the end of the experiment.
    //
    //["sr", "__SendResults__", { }],

    ["sep", "Separator", { }],

    // New in Ibex 0.3-beta19. You can now determine the point in the experiment at which the counter
    // for latin square designs will be updated. (Previously, this was always updated upon completion
    // of the experiment.) To do this, insert the special '__SetCounter__' controller at the desired
    // point in your running order. If given no options, the counter is incremented by one. If given
    // an 'inc' option, the counter is incremented by the specified amount. If given a 'set' option,
    // the counter is set to the given number. (E.g., { set: 100 }, { inc: -1 })
    //
    //["setcounter", "__SetCounter__", { }],

    // NOTE: You could also use the 'Message' controller for the experiment intro (this provides a simple
    // consent checkbox).

    ["intro", "Form", {
        html: { include: "example_intro.html" },
        validators: {
            age: function (s) { if (s.match(/^＼d+$/)) return true; else return "Bad value for ＼u2018age＼u2019"; }
        }
    } ],

    //
    // Three practice items for self-paced reading (one with a comprehension question).
    //
    ["practice", "DashedSentenceNoSpace", {s: "これから 様々な 文が たくさん 出てきます。"},
                 "Question", {q: "１文ずつ文を読みおわると、質問が出てきます。質問に対して、適切な答えを選んでください。",
                              as: ["選択肢1を選ぶには、数字キー「1」を押すか、ここをクリックしてください",
                                   "選択肢2を選ぶには、数字キー「2」を押すか、ここをクリックしてください"],
                              hasCorrect: 0}],
    ["practice", "DashedSentenceNoSpace", {s: "裏庭には 二羽 にわとりが いる。"},
                 "Question", {q: "にわとりは裏庭にいますか？",
                              hasCorrect: 0}],
    ["practice", "DashedSentenceNoSpace", {s: "坊主が 屏風に 上手に 坊主の 絵を 描いた。"},
                 "Question", {q: "坊主の絵は下手でしたか？",
                              hasCorrect: 1}],

    // Experiemntal Items
    // hascorrect: "0" is "yes", "1" is "no"

    //Experiment A (four conditions)
    [["X_a",1], "DashedSentenceNoSpace", {s: "誰もが 花子を 褒めた らしい。"},
               "Question",       {q: "花子は褒められましたか？", hasCorrect:0 }],
    [["X_b",1], "DashedSentenceNoSpace", {s: "みんなが 花子を 褒めた らしい。"},
               "Question",       {q: "花子は褒められましたか？", hasCorrect:0}],

    [["X_a",2], "DashedSentenceNoSpace", {s: "誰もが 太郎を 気に入った らしい。"},
               "Question",       {q: "太郎は気に入られませんでしたか？", hasCorrect:1 }],
    [["X_b",2], "DashedSentenceNoSpace", {s: "みんなが 太郎を 気に入った らしい。"},
               "Question",       {q: "太郎は気に入られませんでしたか？", hasCorrect:1}],


    [["X_a",3], "DashedSentenceNoSpace", {s: "誰もが 次郎を 叱った らしい。"},
                          "Question",       {q: "次郎は叱られませんでしたか？", hasCorrect:1 }],
    [["X_b",3], "DashedSentenceNoSpace", {s: "みんなが 次郎を 叱った らしい。"},
                          "Question",       {q: "次郎は叱られませんでしたか？", hasCorrect:1}],

    [["X_a",4], "DashedSentenceNoSpace", {s: "誰もが 桃子を 祝った らしい。"},
                          "Question",       {q: "桃子は祝福されましたか？", hasCorrect:0 }],
    [["X_b",4], "DashedSentenceNoSpace", {s: "みんなが 桃子を 祝った らしい。"},
                          "Question",       {q: "桃子は祝福されましたか？", hasCorrect:0}],

    // Niikuni & Muramoto 2014
    [["X_a",5], "DashedSentenceNoSpace", {s: "西田さんが、 絵本を 心から 愛した 子どもたちに プレゼントを あげた。"},
                           "Question",       {q: "絵本を愛しているのは西田さんですか？", hasCorrect:1 }],
    [["X_b",5], "DashedSentenceNoSpace", {s: "西田さんが、 絵本を 心から 愛した 子どもたちに プレゼントを あげた。"},
                           "Question",       {q: "絵本を愛しているのは西田さんですか？", hasCorrect:1}],

    // 井上 2006
    [["X_a",6], "DashedSentenceNoSpace", {s: "警官が 犯人を 捕まえた 小林さんに 礼を 言った。"},
                           "Question",       {q: "犯人を捕まえたのは警官ですか？", hasCorrect:1 }],
    [["X_b",6], "DashedSentenceNoSpace", {s: "警官が 犯人を 捕まえた 小林さんに 礼を 言った。"},
                           "Question",       {q: "犯人を捕まえたのは警官ですか？", hasCorrect:1}],

    [["X_a",7], "DashedSentenceNoSpace", {s: "調査官が 関係を 調べた 部下に 結果を 報告させた。"},
                           "Question",       {q: "関係を調べたのは部下ですか？", hasCorrect:0 }],
    [["X_b",7], "DashedSentenceNoSpace", {s: "調査官が 関係を 調べた 部下に 結果を 報告させた。"},
                           "Question",       {q: "関係を調べたのは部下ですか", hasCorrect:0}],

    //Nakamura & Arai 2012
    [["X_a",9], "DashedSentenceNoSpace", {s: "赤ちゃんが ミルクを テーブルに 派手に こぼした 女優を じっと 見つめた。"},
               "Question",       {q: "女優が派手にこぼしたのはミルクですか？", hasCorrect:0 }],
    [["X_b",9], "DashedSentenceNoSpace", {s: "赤ちゃんが ミルクを テーブルに 派手に こぼした 女優を じっと 見つめた。"},
               "Question",       {q: "女優が派手にこぼしたのはミルクですか？", hasCorrect:0}],

    //Experiment B (two  conditions)
    [["Y_a",8], "DashedSentenceNoSpace", {s: "学生が 3冊の 辞書を 昨日 買った らしい。"},
               "Question",       {q: "学生は辞書を買いましたか？", hasCorrect:0 }],
    [["Y_b",8], "DashedSentenceNoSpace", {s: "学生が 辞書を 昨日 3冊 買った らしい。"},
               "Question",       {q: "学生は辞書を買いましたか？", hasCorrect:0}],

    [["Y_a",9], "DashedSentenceNoSpace", {s: "男の子が 2個の ケーキを 今朝 食べた そうだ。"},
               "Question",       {q: "男の子はおまんじゅうを食べましたか？", hasCorrect:1 }],
    [["Y_b",9], "DashedSentenceNoSpace", {s: "男の子が ケーキを 今朝 2個 食べた そうだ。"},
               "Question",       {q: "男の子はおまんじゅうを食べましたか", hasCorrect:1}],

    //[["Y_a",13], "DashedSentenceNoSpace", {s: "店員が 2枚の お皿を 今日 割った そうだ。"},
    //                     "Question",       {q: "店員は昨日お皿を割ってしまいましたか？", hasCorrect:1 }],
    //[["Y_b",13], "DashedSentenceNoSpace", {s: "店員が お皿を 今日 2枚 割った そうだ。"},
    //                     "Question",       {q: "店員は昨日お皿を割ってしまいましたか？", hasCorrect:1}],

    //[["Y_a",14], "DashedSentenceNoSpace", {s: "女の子が 3本の ジュースを 昨夜 飲んだ らしい。"},
    //                     "Question",       {q: "女の子は昨夜ジュースを飲みましたか？", hasCorrect:0 }],
    //[["Y_b",14], "DashedSentenceNoSpace", {s: "女の子が ジュースを 昨夜 3本 飲んだ らしい。"},
    //                     "Question",       {q: "女の子は昨夜ジュースを飲みましたか？", hasCorrect:0}],



    // The first question will be chosen if the first sentence from the previous two items is chosen;
    // the second question will be chosen if the second sentence from the previous pair of items is chosen.
    /*
    [["q1",[100,1]], "AcceptabilityJudgment", {s: "Which actress did the journalist interview after meeting her PA on a previous occasion?"}],
    [["q2",[100,1]], "AcceptabilityJudgment", {s: "Which actress did the journalist interview her husband after meeting on a previous occasion?"}],

    [["s1",2], "DashedSentenceNoSpace", {s: "The teacher helped struggling students who he encouraged to succeed without treating like idiots."},
               "Question",       {q: "What did the teacher do?",
                                  as: ["Encourage struggling students to succeed",
                                       "Encourage his best students to succeed",
                                       "Treat struffling students like idiots"]}],
    [["s2",2], "DashedSentenceNoSpace", {s: "The teacher helped struggling students who without treating like idiots he encouraged to succeed."},
               "Question",       {q: "What did the teacher do?", as: ["Encourage struggling students to succeed",
                                                                      "Encourage his best students to succeed",
                                                                      "Treat struggling students like idiots"]}],

    [["q1",[200,2]], "AcceptabilityJudgment", {s: {html: "<b>Which struggling students</b> did the teacher encourage to succeed without treating their friends like idiots?"}}],
    [["q2",[200,2]], "AcceptabilityJudgment", {s: {html: "<b>Which struggling students</b> did the teacher encourage their friends to succeed without treating like idiots?"}}],

    */
    //
    // 8 self-paced-reading filler sentences.
    //

    //[["f", 101], "DashedSentenceNoSpace", {s: "サーフィンは 五輪の 正式種目に なった。"},
    //      "Question",       {q: "サーフィンはオリンピックの正式種目ですか？",
    //                         hasCorrect:0 }],

    [["f", 101], "DashedSentenceNoSpace", {s: "大統領が 国連の サミットに 突然 現れ、 出席者が 驚いた。"},
          "Question",       {q: "大統領は驚きましたか？",
                            hasCorrect:1}],

    //[["f", 102], "DashedSentenceNoSpace", {s: "そのダンサーだけが ツアーに 参加することを 許された。"},
    //      "Question",       {q: "そのダンサーはツアーに参加できますか？",
    //                         hasCorrect:0 }],

    [["f", 103], "DashedSentenceNoSpace", {s: "彼女は ベナン共和国で 現地の人々とともに 働いている。"},
          "Question",       {q: "彼女はガーナ共和国で働いていますか？",
                             hasCorrect:1 }],

    //[["f", 104], "DashedSentenceNoSpace", {s: "彼は ルノワールの 絵画が 大好きだ。"},
    //      "Question",       {q: "彼が好きなのは ピカソですか？",
    //                         hasCorrect:1}],

    //[["f", 105], "DashedSentenceNoSpace", {s: "ベルギーの 公用語は ３つ ある。"},
    //      "Question",       {q: "ベルギーには複数の公用語がありますか？",
    //                         hasCorrect:0 }],

    //[["f", 106], "DashedSentenceNoSpace", {s: "ハカは マオリ族の 民族舞踊だ。"},
    //      "Question",       {q: "ハカはアボリジニの民族舞踊ですか？",
    //                         hasCorrect:1}],

    [["f", 107], "DashedSentenceNoSpace", {s: "友人は カナダで オーロラを 見た。"},
          "Question",       {q: "友人はオーロラを見ましたか？",
                             hasCorrect:0 }],

    //[["f",108],"DashedSentence", {s: "John talk_to the_professor in_the_park"}],
    [["f",108],"DashedSentence", {s: ["John", "talk to", "the professor", "in the_park"]}],                        

];
