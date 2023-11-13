from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_transcription')
def get_transcription():
    transcription_data = [
		{
			"timestamps": {
				"from": "00:00:00,000",
				"to": "00:00:07,280"
			},
			"offsets": {
				"from": 0,
				"to": 7280
			},
			"text": " Hi, I'm Lucas. I'm the TOEFL expert at Magoosh.com and in this video you're going to get some"
		},
		{
			"timestamps": {
				"from": "00:00:07,280",
				"to": "00:00:14,400"
			},
			"offsets": {
				"from": 7280,
				"to": 14400
			},
			"text": " listening practice that's just like listening on the real TOEFL. But first let me introduce you to"
		},
		{
			"timestamps": {
				"from": "00:00:14,400",
				"to": "00:00:22,320"
			},
			"offsets": {
				"from": 14400,
				"to": 22320
			},
			"text": " the listening section so you know what to expect. You're going to see or hear three recordings."
		},
		{
			"timestamps": {
				"from": "00:00:22,320",
				"to": "00:00:30,400"
			},
			"offsets": {
				"from": 22320,
				"to": 30400
			},
			"text": " This is a full set on the TOEFL listening but in a real TOEFL you'll have two sets with six"
		},
		{
			"timestamps": {
				"from": "00:00:30,400",
				"to": "00:00:37,600"
			},
			"offsets": {
				"from": 30400,
				"to": 37600
			},
			"text": " recordings all together. Here in this video we'll do just three and in that set of three you're"
		},
		{
			"timestamps": {
				"from": "00:00:37,600",
				"to": "00:00:45,360"
			},
			"offsets": {
				"from": 37600,
				"to": 45360
			},
			"text": " going to hear a conversation between two students, a lecture from a professor and a classroom"
		},
		{
			"timestamps": {
				"from": "00:00:45,360",
				"to": "00:00:53,280"
			},
			"offsets": {
				"from": 45360,
				"to": 53280
			},
			"text": " discussion with a professor and students talking together in class. Each of those recordings you"
		},
		{
			"timestamps": {
				"from": "00:00:53,280",
				"to": "00:01:01,840"
			},
			"offsets": {
				"from": 53280,
				"to": 61840
			},
			"text": " should hear only one time. Do not stop the video when you're listening. Do not rewind and listen again."
		},
		{
			"timestamps": {
				"from": "00:01:01,840",
				"to": "00:01:09,840"
			},
			"offsets": {
				"from": 61840,
				"to": 69840
			},
			"text": " Just listen once and take notes because after every recording you're going to see questions."
		},
		{
			"timestamps": {
				"from": "00:01:09,840",
				"to": "00:01:19,200"
			},
			"offsets": {
				"from": 69840,
				"to": 79200
			},
			"text": " Five or six multiple choice questions meaning A, B, C or D. Write your answer as the question is on"
		},
		{
			"timestamps": {
				"from": "00:01:19,200",
				"to": "00:01:26,400"
			},
			"offsets": {
				"from": 79200,
				"to": 86400
			},
			"text": " the screen. Similar to the real test you'll have about 30 seconds per question so we will keep"
		},
		{
			"timestamps": {
				"from": "00:01:26,400",
				"to": "00:01:32,800"
			},
			"offsets": {
				"from": 86400,
				"to": 92800
			},
			"text": " that question on the screen in the video for about 30 seconds and in that time you should write down"
		},
		{
			"timestamps": {
				"from": "00:01:32,800",
				"to": "00:01:41,120"
			},
			"offsets": {
				"from": 92800,
				"to": 101120
			},
			"text": " your answer A, B, C or D after looking at your notes from what you heard before and then you'll see the"
		},
		{
			"timestamps": {
				"from": "00:01:41,120",
				"to": "00:01:49,040"
			},
			"offsets": {
				"from": 101120,
				"to": 109040
			},
			"text": " next question. At the end of all three recordings with all of their questions you'll see the answers"
		},
		{
			"timestamps": {
				"from": "00:01:49,040",
				"to": "00:01:55,840"
			},
			"offsets": {
				"from": 109040,
				"to": 115840
			},
			"text": " so you can grade your answers and find out which ones you got right and which ones you got wrong."
		},
		{
			"timestamps": {
				"from": "00:01:55,840",
				"to": "00:02:02,720"
			},
			"offsets": {
				"from": 115840,
				"to": 122720
			},
			"text": " So you can learn from your mistakes and know how to improve before test day. Okay so let's get"
		},
		{
			"timestamps": {
				"from": "00:02:02,720",
				"to": "00:02:09,920"
			},
			"offsets": {
				"from": 122720,
				"to": 129920
			},
			"text": " started. You're going to hear the first recording next and then the first set of questions and after"
		},
		{
			"timestamps": {
				"from": "00:02:09,920",
				"to": "00:02:14,240"
			},
			"offsets": {
				"from": 129920,
				"to": 134240
			},
			"text": " that the second recording with the second set of questions etc."
		},
		{
			"timestamps": {
				"from": "00:02:14,240",
				"to": "00:02:20,400"
			},
			"offsets": {
				"from": 134240,
				"to": 140400
			},
			"text": " Now listen to a conversation between a student and a professor."
		},
		{
			"timestamps": {
				"from": "00:02:20,400",
				"to": "00:02:25,360"
			},
			"offsets": {
				"from": 140400,
				"to": 145360
			},
			"text": " So Erin in your email you said you wanted to talk about the exam."
		},
		{
			"timestamps": {
				"from": "00:02:25,360",
				"to": "00:02:32,400"
			},
			"offsets": {
				"from": 145360,
				"to": 152400
			},
			"text": " Yeah um I've just never taken a class with so many different readings. I've managed to keep"
		},
		{
			"timestamps": {
				"from": "00:02:32,400",
				"to": "00:02:41,120"
			},
			"offsets": {
				"from": 152400,
				"to": 161120
			},
			"text": " up with all the assignments but I'm not sure how to how to how to review everything. Yeah in other"
		},
		{
			"timestamps": {
				"from": "00:02:41,120",
				"to": "00:02:46,320"
			},
			"offsets": {
				"from": 161120,
				"to": 166320
			},
			"text": " classes I've had there's usually just one book to review not three different books plus all"
		},
		{
			"timestamps": {
				"from": "00:02:46,320",
				"to": "00:02:54,320"
			},
			"offsets": {
				"from": 166320,
				"to": 174320
			},
			"text": " those other text excerpts and videos. Well developmental psychology is a little more involved compared"
		},
		{
			"timestamps": {
				"from": "00:02:54,320",
				"to": "00:03:01,920"
			},
			"offsets": {
				"from": 174320,
				"to": 181920
			},
			"text": " to some other subjects. You've looked at the study guide I assume. Kind of yes I mean"
		},
		{
			"timestamps": {
				"from": "00:03:02,640",
				"to": "00:03:07,520"
			},
			"offsets": {
				"from": 182640,
				"to": 187520
			},
			"text": " I haven't gone through the whole thing yet I'm still just doing the stuff on the first page."
		},
		{
			"timestamps": {
				"from": "00:03:07,520",
				"to": "00:03:11,520"
			},
			"offsets": {
				"from": 187520,
				"to": 191520
			},
			"text": " You haven't looked at the second page of the study guide at all yet?"
		},
		{
			"timestamps": {
				"from": "00:03:11,520",
				"to": "00:03:16,800"
			},
			"offsets": {
				"from": 191520,
				"to": 196800
			},
			"text": " No I've barely had time to go back over the first two readings from the first page."
		},
		{
			"timestamps": {
				"from": "00:03:16,800",
				"to": "00:03:23,360"
			},
			"offsets": {
				"from": 196800,
				"to": 203360
			},
			"text": " Well no wonder you're so confused about where to start. Let me show you a copy of the study guide."
		},
		{
			"timestamps": {
				"from": "00:03:23,360",
				"to": "00:03:30,000"
			},
			"offsets": {
				"from": 203360,
				"to": 210000
			},
			"text": " Look here see what it says at the top of the page. This first page is just a list of all the"
		},
		{
			"timestamps": {
				"from": "00:03:30,000",
				"to": "00:03:38,000"
			},
			"offsets": {
				"from": 210000,
				"to": 218000
			},
			"text": " text and videos that will be on the test. The actual guide is on the second page. See? Oh wow and it says"
		},
		{
			"timestamps": {
				"from": "00:03:38,000",
				"to": "00:03:44,960"
			},
			"offsets": {
				"from": 218000,
				"to": 224960
			},
			"text": " what I need to remember from each reading. Uh huh so for example from the intro to adolescent"
		},
		{
			"timestamps": {
				"from": "00:03:44,960",
				"to": "00:03:50,720"
			},
			"offsets": {
				"from": 224960,
				"to": 230720
			},
			"text": " psychology book you only need to review the developmental stages from chapter two. And it looks"
		},
		{
			"timestamps": {
				"from": "00:03:50,720",
				"to": "00:03:57,200"
			},
			"offsets": {
				"from": 230720,
				"to": 237200
			},
			"text": " like I need to know everything from the main textbook the big one. Right you'll want to review"
		},
		{
			"timestamps": {
				"from": "00:03:57,200",
				"to": "00:04:03,440"
			},
			"offsets": {
				"from": 237200,
				"to": 243440
			},
			"text": " all the core concepts in the first four chapters of development through lifespan. Well almost all."
		},
		{
			"timestamps": {
				"from": "00:04:03,440",
				"to": "00:04:08,560"
			},
			"offsets": {
				"from": 243440,
				"to": 248560
			},
			"text": " I forgot to mention this on the study guide but the test won't really go into Freud stages of"
		},
		{
			"timestamps": {
				"from": "00:04:08,560",
				"to": "00:04:15,040"
			},
			"offsets": {
				"from": 248560,
				"to": 255040
			},
			"text": " development. Those are a little outdated compared to newer research. But we're still going"
		},
		{
			"timestamps": {
				"from": "00:04:15,040",
				"to": "00:04:21,040"
			},
			"offsets": {
				"from": 255040,
				"to": 261040
			},
			"text": " over all of Piaget's developmental stages for children right? Exactly. And notice that you only"
		},
		{
			"timestamps": {
				"from": "00:04:21,040",
				"to": "00:04:25,920"
			},
			"offsets": {
				"from": 261040,
				"to": 265920
			},
			"text": " need to review about half of the supplemental readings. Just the ones that focus on adult"
		},
		{
			"timestamps": {
				"from": "00:04:25,920",
				"to": "00:04:32,960"
			},
			"offsets": {
				"from": 265920,
				"to": 272960
			},
			"text": " psychological development and the video on Alzheimer's disease. The brain disorder and elderly people. See"
		},
		{
			"timestamps": {
				"from": "00:04:32,960",
				"to": "00:04:42,000"
			},
			"offsets": {
				"from": 272960,
				"to": 282000
			},
			"text": " I marked it right here. Okay I feel like I understand a lot better now. I uh I guess I should have"
		},
		{
			"timestamps": {
				"from": "00:04:42,000",
				"to": "00:04:49,200"
			},
			"offsets": {
				"from": 282000,
				"to": 289200
			},
			"text": " looked at the second page huh? Yeah and I actually did mention that in class. You know you really"
		},
		{
			"timestamps": {
				"from": "00:04:49,200",
				"to": "00:04:54,560"
			},
			"offsets": {
				"from": 289200,
				"to": 294560
			},
			"text": " should have checked with your classmates before coming to me. Well I've always studied alone before."
		},
		{
			"timestamps": {
				"from": "00:04:55,200",
				"to": "00:05:00,960"
			},
			"offsets": {
				"from": 295200,
				"to": 300960
			},
			"text": " I don't think students should be studying solo in any class. It's always better to study with a partner or"
		},
		{
			"timestamps": {
				"from": "00:05:00,960",
				"to": "00:05:08,800"
			},
			"offsets": {
				"from": 300960,
				"to": 308800
			},
			"text": " a group. It can really help avoid confusion. Yeah I've really had trouble keeping up in class so far."
		},
		{
			"timestamps": {
				"from": "00:05:08,800",
				"to": "00:05:15,360"
			},
			"offsets": {
				"from": 308800,
				"to": 315360
			},
			"text": " I think I'll join the class study group in the library tonight. Yeah please do. Your classmates can"
		},
		{
			"timestamps": {
				"from": "00:05:15,360",
				"to": "00:05:20,400"
			},
			"offsets": {
				"from": 315360,
				"to": 320400
			},
			"text": " probably help you more than I could. You know when it comes to organizing your notes, getting"
		},
		{
			"timestamps": {
				"from": "00:05:20,400",
				"to": "00:05:30,160"
			},
			"offsets": {
				"from": 320400,
				"to": 330160
			},
			"text": " together a good study strategy, that sort of thing? Why does the student visit her professor?"
		},
		{
			"timestamps": {
				"from": "00:05:30,160",
				"to": "00:06:00,000"
			},
			"offsets": {
				"from": 330160,
				"to": 360000
			},
			"text": " Why does the student think reviewing for the test is especially hard in her psychology class?"
		},
		{
			"timestamps": {
				"from": "00:06:00,000",
				"to": "00:06:27,360"
			},
			"offsets": {
				"from": 360000,
				"to": 387360
			},
			"text": " What is the professor's attitude towards study groups?"
		},
		{
			"timestamps": {
				"from": "00:06:27,360",
				"to": "00:06:53,360"
			},
			"offsets": {
				"from": 387360,
				"to": 413360
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:06:54,080",
				"to": "00:07:04,880"
			},
			"offsets": {
				"from": 414080,
				"to": 424880
			},
			"text": " What does the professor imply the student should do if she has any more questions about the exam?"
		},
		{
			"timestamps": {
				"from": "00:07:23,680",
				"to": "00:07:30,000"
			},
			"offsets": {
				"from": 443680,
				"to": 450000
			},
			"text": " Listen again to part of the conversation then answer the question. And notice that you only need to"
		},
		{
			"timestamps": {
				"from": "00:07:30,000",
				"to": "00:07:35,280"
			},
			"offsets": {
				"from": 450000,
				"to": 455280
			},
			"text": " review about half of the supplemental readings. Just the ones that focus on adult psychological"
		},
		{
			"timestamps": {
				"from": "00:07:35,280",
				"to": "00:07:42,080"
			},
			"offsets": {
				"from": 455280,
				"to": 462080
			},
			"text": " development and the video on Alzheimer's disease, the brain disorder and elderly people. See I marked it"
		},
		{
			"timestamps": {
				"from": "00:07:42,080",
				"to": "00:07:49,040"
			},
			"offsets": {
				"from": 462080,
				"to": 469040
			},
			"text": " right here. Why does the professor say this? And the video on Alzheimer's disease, the brain"
		},
		{
			"timestamps": {
				"from": "00:07:49,040",
				"to": "00:07:54,480"
			},
			"offsets": {
				"from": 469040,
				"to": 474480
			},
			"text": " disorder and elderly people. See I marked it right here."
		},
		{
			"timestamps": {
				"from": "00:07:54,480",
				"to": "00:08:23,440"
			},
			"offsets": {
				"from": 474480,
				"to": 503440
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:08:23,440",
				"to": "00:08:31,360"
			},
			"offsets": {
				"from": 503440,
				"to": 511360
			},
			"text": " Listen to part of a lecture in a geology class. You'll recall that soil erosion is a process where"
		},
		{
			"timestamps": {
				"from": "00:08:31,360",
				"to": "00:08:37,120"
			},
			"offsets": {
				"from": 511360,
				"to": 517120
			},
			"text": " soil is worn away over time. We've looked at the ways the wind can move soil, pull it apart,"
		},
		{
			"timestamps": {
				"from": "00:08:37,120",
				"to": "00:08:43,680"
			},
			"offsets": {
				"from": 517120,
				"to": 523680
			},
			"text": " blow it away. Now I'm going to tell you about some of the ways that rainwater can erode soil."
		},
		{
			"timestamps": {
				"from": "00:08:43,680",
				"to": "00:08:52,080"
			},
			"offsets": {
				"from": 523680,
				"to": 532080
			},
			"text": " Remember soil is very loose, gets very soft when it's wet. So water can have a real impact."
		},
		{
			"timestamps": {
				"from": "00:08:52,480",
				"to": "00:08:58,560"
			},
			"offsets": {
				"from": 532480,
				"to": 538560
			},
			"text": " There are a few different types of soil erosion caused by rain. Water behaves a little differently"
		},
		{
			"timestamps": {
				"from": "00:08:58,560",
				"to": "00:09:06,160"
			},
			"offsets": {
				"from": 538560,
				"to": 546160
			},
			"text": " for each type of erosion and the effects are different. For some context, let's consider bank erosion"
		},
		{
			"timestamps": {
				"from": "00:09:06,160",
				"to": "00:09:12,400"
			},
			"offsets": {
				"from": 546160,
				"to": 552400
			},
			"text": " first. This kind of wearing away of the soil happens along the banks of rivers and streams"
		},
		{
			"timestamps": {
				"from": "00:09:12,400",
				"to": "00:09:19,360"
			},
			"offsets": {
				"from": 552400,
				"to": 559360
			},
			"text": " hence the name. The soil nearest to the water loosens up and starts to wash away. Plants growing"
		},
		{
			"timestamps": {
				"from": "00:09:19,360",
				"to": "00:09:25,920"
			},
			"offsets": {
				"from": 559360,
				"to": 565920
			},
			"text": " in the soil come loose too. Grass, bushes, even trees can eventually fall into running water."
		},
		{
			"timestamps": {
				"from": "00:09:25,920",
				"to": "00:09:31,200"
			},
			"offsets": {
				"from": 565920,
				"to": 571200
			},
			"text": " If you look at the edge of a river, you can notice this. The way that the land along the river"
		},
		{
			"timestamps": {
				"from": "00:09:31,200",
				"to": "00:09:36,480"
			},
			"offsets": {
				"from": 571200,
				"to": 576480
			},
			"text": " seems to hang out over the water with the current under the edge of the land. This is because"
		},
		{
			"timestamps": {
				"from": "00:09:36,480",
				"to": "00:09:42,960"
			},
			"offsets": {
				"from": 576480,
				"to": 582960
			},
			"text": " the soil beneath the bank has been eaten away. The effects of this are pretty clear. I'm sure you"
		},
		{
			"timestamps": {
				"from": "00:09:42,960",
				"to": "00:09:49,120"
			},
			"offsets": {
				"from": 582960,
				"to": 589120
			},
			"text": " can all picture it well enough. The first significant stage of rain erosion is a bit harder to"
		},
		{
			"timestamps": {
				"from": "00:09:49,120",
				"to": "00:09:56,640"
			},
			"offsets": {
				"from": 589120,
				"to": 596640
			},
			"text": " spot. We call it \"Sheet erosion\". This process happens more slowly. It'll happen on land that's"
		},
		{
			"timestamps": {
				"from": "00:09:56,640",
				"to": "00:10:04,880"
			},
			"offsets": {
				"from": 596640,
				"to": 604880
			},
			"text": " sloped, slanted in one direction or another. As gravity pulls rain down a slope, the rain grabs some"
		},
		{
			"timestamps": {
				"from": "00:10:04,880",
				"to": "00:10:11,680"
			},
			"offsets": {
				"from": 604880,
				"to": 611680
			},
			"text": " soil, takes it along for the ride. Hills will seem more sandy than level ground because they've"
		},
		{
			"timestamps": {
				"from": "00:10:11,680",
				"to": "00:10:18,320"
			},
			"offsets": {
				"from": 611680,
				"to": 618320
			},
			"text": " lost some of their soil to sheet erosion. But this effect happens even on land that's just a little"
		},
		{
			"timestamps": {
				"from": "00:10:18,320",
				"to": "00:10:25,040"
			},
			"offsets": {
				"from": 618320,
				"to": 625040
			},
			"text": " tilted. It just happens more slowly. It can take years to really make a difference, but eventually it"
		},
		{
			"timestamps": {
				"from": "00:10:25,040",
				"to": "00:10:32,480"
			},
			"offsets": {
				"from": 625040,
				"to": 632480
			},
			"text": " really does. Very gradually, rain will strip away the soil and pull it to the bottom of the slope,"
		},
		{
			"timestamps": {
				"from": "00:10:32,480",
				"to": "00:10:37,840"
			},
			"offsets": {
				"from": 632480,
				"to": 637840
			},
			"text": " and the higher land will become sandy. Plants will start to struggle and die off."
		},
		{
			"timestamps": {
				"from": "00:10:37,840",
				"to": "00:10:45,600"
			},
			"offsets": {
				"from": 637840,
				"to": 645600
			},
			"text": " Sheet erosion really only happens on slopes that are smooth, so that the rainwater flows in one big"
		},
		{
			"timestamps": {
				"from": "00:10:45,600",
				"to": "00:10:52,320"
			},
			"offsets": {
				"from": 645600,
				"to": 652320
			},
			"text": " sheet flows evenly across the whole slope. This doesn't really leave room for that bank erosion I"
		},
		{
			"timestamps": {
				"from": "00:10:52,320",
				"to": "00:10:58,800"
			},
			"offsets": {
				"from": 652320,
				"to": 658800
			},
			"text": " mentioned earlier. It's just an initial stage, but once the slope is a little more bumpy,"
		},
		{
			"timestamps": {
				"from": "00:10:58,800",
				"to": "00:11:05,920"
			},
			"offsets": {
				"from": 658800,
				"to": 665920
			},
			"text": " with uneven soil, erosion will happen less evenly too. When it rains, water will naturally"
		},
		{
			"timestamps": {
				"from": "00:11:05,920",
				"to": "00:11:12,160"
			},
			"offsets": {
				"from": 665920,
				"to": 672160
			},
			"text": " flow through the lowest smoothest path on the slope. It'll flow around the bumps. In other words,"
		},
		{
			"timestamps": {
				"from": "00:11:12,640",
				"to": "00:11:20,080"
			},
			"offsets": {
				"from": 672640,
				"to": 680080
			},
			"text": " and form tiny streams, I mean not real streams, just little paths of flowing rainwater."
		},
		{
			"timestamps": {
				"from": "00:11:20,080",
				"to": "00:11:27,840"
			},
			"offsets": {
				"from": 680080,
				"to": 687840
			},
			"text": " These flows are called reels. Soil from the higher parts of the land can get washed into the"
		},
		{
			"timestamps": {
				"from": "00:11:27,840",
				"to": "00:11:34,320"
			},
			"offsets": {
				"from": 687840,
				"to": 694320
			},
			"text": " real a little, but most of the erosion happens to the soil that's directly in the reels path."
		},
		{
			"timestamps": {
				"from": "00:11:34,320",
				"to": "00:11:41,680"
			},
			"offsets": {
				"from": 694320,
				"to": 701680
			},
			"text": " This soil gets washed away to lower ground, and the real erosion makes a sandy path through"
		},
		{
			"timestamps": {
				"from": "00:11:41,680",
				"to": "00:11:49,200"
			},
			"offsets": {
				"from": 701680,
				"to": 709200
			},
			"text": " the surrounding dirt. A path you can see even when it's not raining. Reels can change the shape of an open"
		},
		{
			"timestamps": {
				"from": "00:11:49,200",
				"to": "00:11:56,640"
			},
			"offsets": {
				"from": 709200,
				"to": 716640
			},
			"text": " surface, as the soils pushed forward, big lumps of it can form in the real and not move all the way"
		},
		{
			"timestamps": {
				"from": "00:11:56,640",
				"to": "00:12:03,120"
			},
			"offsets": {
				"from": 716640,
				"to": 723120
			},
			"text": " down the slope. So the real will have new different bumps to flow around the next time it rains."
		},
		{
			"timestamps": {
				"from": "00:12:03,120",
				"to": "00:12:10,720"
			},
			"offsets": {
				"from": 723120,
				"to": 730720
			},
			"text": " A real can change its path completely, eventually. On the other hand, sometimes it doesn't change"
		},
		{
			"timestamps": {
				"from": "00:12:10,720",
				"to": "00:12:17,840"
			},
			"offsets": {
				"from": 730720,
				"to": 737840
			},
			"text": " all that much. Just goes along pretty much the same path every time it rains. Reels can get really deep"
		},
		{
			"timestamps": {
				"from": "00:12:17,840",
				"to": "00:12:24,800"
			},
			"offsets": {
				"from": 737840,
				"to": 744800
			},
			"text": " if that happens, widening at the same time. Via the bank erosion process I mentioned earlier."
		},
		{
			"timestamps": {
				"from": "00:12:24,800",
				"to": "00:12:32,080"
			},
			"offsets": {
				"from": 744800,
				"to": 752080
			},
			"text": " They can develop into a more dramatic groove that's all sand and no soil. Kind of looks like a"
		},
		{
			"timestamps": {
				"from": "00:12:32,080",
				"to": "00:12:40,560"
			},
			"offsets": {
				"from": 752080,
				"to": 760560
			},
			"text": " dry river bed. A big real like that is called a gully. Gully erosion can really mess up a piece of land."
		},
		{
			"timestamps": {
				"from": "00:12:41,120",
				"to": "00:12:47,200"
			},
			"offsets": {
				"from": 761120,
				"to": 767200
			},
			"text": " Pull the soil away from the land in large strips so that big pieces of land are no longer plant"
		},
		{
			"timestamps": {
				"from": "00:12:47,200",
				"to": "00:12:53,600"
			},
			"offsets": {
				"from": 767200,
				"to": 773600
			},
			"text": " friendly at all. There are actually more types, but it's these that will need to understand the"
		},
		{
			"timestamps": {
				"from": "00:12:53,600",
				"to": "00:12:59,760"
			},
			"offsets": {
				"from": 773600,
				"to": 779760
			},
			"text": " process. The progression toward barren land made when soil is left vulnerable to the effects of"
		},
		{
			"timestamps": {
				"from": "00:12:59,760",
				"to": "00:13:06,000"
			},
			"offsets": {
				"from": 779760,
				"to": 786000
			},
			"text": " rain. Farm land between harvests, deforestation expanses, and less they're covered and protected,"
		},
		{
			"timestamps": {
				"from": "00:13:06,000",
				"to": "00:13:13,760"
			},
			"offsets": {
				"from": 786000,
				"to": 793760
			},
			"text": " the soil will start moving. What aspect of water erosion does the lecture focus on?"
		},
		{
			"timestamps": {
				"from": "00:13:13,760",
				"to": "00:13:43,520"
			},
			"offsets": {
				"from": 793760,
				"to": 823520
			},
			"text": " According to the lecture, what are the physical effects of bank erosion?"
		},
		{
			"timestamps": {
				"from": "00:13:43,520",
				"to": "00:14:13,280"
			},
			"offsets": {
				"from": 823520,
				"to": 853280
			},
			"text": " Choose two answers. According to the professor, what is the effect of sheet erosion on plant life?"
		},
		{
			"timestamps": {
				"from": "00:14:13,280",
				"to": "00:14:41,440"
			},
			"offsets": {
				"from": 853280,
				"to": 881440
			},
			"text": " What can be inferred about how reels are formed?"
		},
		{
			"timestamps": {
				"from": "00:14:41,440",
				"to": "00:15:09,840"
			},
			"offsets": {
				"from": 881440,
				"to": 909840
			},
			"text": " When does gully erosion happen?"
		},
		{
			"timestamps": {
				"from": "00:15:09,840",
				"to": "00:15:39,680"
			},
			"offsets": {
				"from": 909840,
				"to": 939680
			},
			"text": " Listen again to part of the lecture."
		},
		{
			"timestamps": {
				"from": "00:15:39,680",
				"to": "00:15:47,680"
			},
			"offsets": {
				"from": 939680,
				"to": 947680
			},
			"text": " Then answer the question. Hills will seem more sandy than level ground because they've lost some of"
		},
		{
			"timestamps": {
				"from": "00:15:47,680",
				"to": "00:15:54,720"
			},
			"offsets": {
				"from": 947680,
				"to": 954720
			},
			"text": " their soil to sheet erosion, but this effect happens even on land that's just a little tilted. It just"
		},
		{
			"timestamps": {
				"from": "00:15:54,720",
				"to": "00:16:01,120"
			},
			"offsets": {
				"from": 954720,
				"to": 961120
			},
			"text": " happens more slowly. It can take years to really make a difference, but eventually it really does."
		},
		{
			"timestamps": {
				"from": "00:16:02,640",
				"to": "00:16:09,360"
			},
			"offsets": {
				"from": 962640,
				"to": 969360
			},
			"text": " What does the professor imply when she says this? It can take years to really make a difference,"
		},
		{
			"timestamps": {
				"from": "00:16:09,360",
				"to": "00:16:13,600"
			},
			"offsets": {
				"from": 969360,
				"to": 973600
			},
			"text": " but eventually it really does."
		},
		{
			"timestamps": {
				"from": "00:16:13,600",
				"to": "00:16:41,440"
			},
			"offsets": {
				"from": 973600,
				"to": 1001440
			},
			"text": " Listen to part of the lecture."
		},
		{
			"timestamps": {
				"from": "00:16:42,640",
				"to": "00:16:45,840"
			},
			"offsets": {
				"from": 1002640,
				"to": 1005840
			},
			"text": " Listen to part of a lecture in a physics class."
		},
		{
			"timestamps": {
				"from": "00:16:45,840",
				"to": "00:16:53,120"
			},
			"offsets": {
				"from": 1005840,
				"to": 1013120
			},
			"text": " So we obviously know that gravity causes things to fall to the ground and stay there."
		},
		{
			"timestamps": {
				"from": "00:16:53,120",
				"to": "00:16:59,040"
			},
			"offsets": {
				"from": 1013120,
				"to": 1019040
			},
			"text": " Controls or bits causes the tides. At least all this seems obvious now,"
		},
		{
			"timestamps": {
				"from": "00:16:59,040",
				"to": "00:17:05,360"
			},
			"offsets": {
				"from": 1019040,
				"to": 1025360
			},
			"text": " but for the longest time gravity was a mystery to scientists. It took thousands of years for"
		},
		{
			"timestamps": {
				"from": "00:17:05,360",
				"to": "00:17:10,480"
			},
			"offsets": {
				"from": 1025360,
				"to": 1030480
			},
			"text": " scientists all around the world to work out how the different effects are connected,"
		},
		{
			"timestamps": {
				"from": "00:17:10,480",
				"to": "00:17:15,920"
			},
			"offsets": {
				"from": 1030480,
				"to": 1035920
			},
			"text": " how this invisible force does its thing. Suzy, you have a question."
		},
		{
			"timestamps": {
				"from": "00:17:15,920",
				"to": "00:17:25,520"
			},
			"offsets": {
				"from": 1035920,
				"to": 1045520
			},
			"text": " Well, yeah, I mean thousands of years. I thought Newton didn't discover gravity until"
		},
		{
			"timestamps": {
				"from": "00:17:25,520",
				"to": "00:17:31,280"
			},
			"offsets": {
				"from": 1045520,
				"to": 1051280
			},
			"text": " like the 1700s. That's less than a thousand years ago."
		},
		{
			"timestamps": {
				"from": "00:17:32,000",
				"to": "00:17:39,920"
			},
			"offsets": {
				"from": 1052000,
				"to": 1059920
			},
			"text": " Oh, um, 1600s actually, but I'm glad you brought him up. Newton is important. He's"
		},
		{
			"timestamps": {
				"from": "00:17:39,920",
				"to": "00:17:46,480"
			},
			"offsets": {
				"from": 1059920,
				"to": 1066480
			},
			"text": " kind of the opposite of the first gravity scientist though. Newton actually finalize much of what"
		},
		{
			"timestamps": {
				"from": "00:17:46,480",
				"to": "00:17:53,120"
			},
			"offsets": {
				"from": 1066480,
				"to": 1073120
			},
			"text": " we know about gravity, what it actually does. A lot of scientists looked at gravity before he did."
		},
		{
			"timestamps": {
				"from": "00:17:53,120",
				"to": "00:17:59,680"
			},
			"offsets": {
				"from": 1073120,
				"to": 1079680
			},
			"text": " There were the engines like Aristotle, the ancient Greek philosopher. He believed every object had"
		},
		{
			"timestamps": {
				"from": "00:17:59,680",
				"to": "00:18:06,640"
			},
			"offsets": {
				"from": 1079680,
				"to": 1086640
			},
			"text": " its own gravity. And this is why a feather would fall slower than a stone. Aristotle would say it had"
		},
		{
			"timestamps": {
				"from": "00:18:06,640",
				"to": "00:18:12,320"
			},
			"offsets": {
				"from": 1086640,
				"to": 1092320
			},
			"text": " less gravity inside it, less than the rock did. Roger, it looks like you have something to say."
		},
		{
			"timestamps": {
				"from": "00:18:12,320",
				"to": "00:18:23,520"
			},
			"offsets": {
				"from": 1092320,
				"to": 1103520
			},
			"text": " Didn't Aristotle also think that some things fell up? I mean, instead of falling down,"
		},
		{
			"timestamps": {
				"from": "00:18:25,200",
				"to": "00:18:32,880"
			},
			"offsets": {
				"from": 1105200,
				"to": 1112880
			},
			"text": " that's a very good point, Roger. Yes. Well, it's a very confusing idea Aristotle had. He believed"
		},
		{
			"timestamps": {
				"from": "00:18:32,880",
				"to": "00:18:39,440"
			},
			"offsets": {
				"from": 1112880,
				"to": 1119440
			},
			"text": " that the gravity in things didn't just determine how fast they fell, but what direction they fell in."
		},
		{
			"timestamps": {
				"from": "00:18:39,440",
				"to": "00:18:45,360"
			},
			"offsets": {
				"from": 1119440,
				"to": 1125360
			},
			"text": " So to Aristotle, the earth was the center of the universe. And he believed most things in the"
		},
		{
			"timestamps": {
				"from": "00:18:45,360",
				"to": "00:18:52,560"
			},
			"offsets": {
				"from": 1125360,
				"to": 1132560
			},
			"text": " universe had a gravity that naturally pulled them to the center, to the ground. But Aristotle"
		},
		{
			"timestamps": {
				"from": "00:18:52,560",
				"to": "00:18:58,320"
			},
			"offsets": {
				"from": 1132560,
				"to": 1138320
			},
			"text": " also believed that certain other things had different natural places. For example,"
		},
		{
			"timestamps": {
				"from": "00:18:58,320",
				"to": "00:19:04,720"
			},
			"offsets": {
				"from": 1138320,
				"to": 1144720
			},
			"text": " fire. Aristotle thought that flames pointed upward because the natural place for a flame was up in"
		},
		{
			"timestamps": {
				"from": "00:19:04,720",
				"to": "00:19:10,240"
			},
			"offsets": {
				"from": 1144720,
				"to": 1150240
			},
			"text": " the air above the earth. But below the moon. Is that what you are getting at, Roger?"
		},
		{
			"timestamps": {
				"from": "00:19:10,240",
				"to": "00:19:18,240"
			},
			"offsets": {
				"from": 1150240,
				"to": 1158240
			},
			"text": " Yeah, I guess. I just thought Aristotle thought flames kept going up and up and up."
		},
		{
			"timestamps": {
				"from": "00:19:19,360",
				"to": "00:19:25,200"
			},
			"offsets": {
				"from": 1159360,
				"to": 1165200
			},
			"text": " No, Aristotle thought the flames would stop at some point at their natural place in the sky."
		},
		{
			"timestamps": {
				"from": "00:19:25,200",
				"to": "00:19:31,680"
			},
			"offsets": {
				"from": 1165200,
				"to": 1171680
			},
			"text": " But I can understand how you'd be confused. Aristotle's ideas seemed odd to us today."
		},
		{
			"timestamps": {
				"from": "00:19:31,680",
				"to": "00:19:37,280"
			},
			"offsets": {
				"from": 1171680,
				"to": 1177280
			},
			"text": " Now, there was another early scientist whose ideas on gravity may seem more familiar."
		},
		{
			"timestamps": {
				"from": "00:19:37,280",
				"to": "00:19:42,720"
			},
			"offsets": {
				"from": 1177280,
				"to": 1182720
			},
			"text": " An ancient Indian thinker from the five hundreds, Brahma Gupta, that was his name."
		},
		{
			"timestamps": {
				"from": "00:19:42,720",
				"to": "00:19:48,000"
			},
			"offsets": {
				"from": 1182720,
				"to": 1188000
			},
			"text": " He believed that the earth was basically a giant ball that was full of gravity and pulled things"
		},
		{
			"timestamps": {
				"from": "00:19:48,000",
				"to": "00:19:55,280"
			},
			"offsets": {
				"from": 1188000,
				"to": 1195280
			},
			"text": " down to it. So, around earth, with its own gravitational pull, just like we believe today."
		},
		{
			"timestamps": {
				"from": "00:19:55,280",
				"to": "00:20:05,920"
			},
			"offsets": {
				"from": 1195280,
				"to": 1205920
			},
			"text": " Now, uh, yes, Suzy. Sorry. I, I'm confused again. I thought nobody knew the earth was round until"
		},
		{
			"timestamps": {
				"from": "00:20:05,920",
				"to": "00:20:15,920"
			},
			"offsets": {
				"from": 1205920,
				"to": 1215920
			},
			"text": " people sailed all the way around the world in, in like the 14 or 1500s. How did Brahma Gupta"
		},
		{
			"timestamps": {
				"from": "00:20:16,720",
				"to": "00:20:24,640"
			},
			"offsets": {
				"from": 1216720,
				"to": 1224640
			},
			"text": " figure out the world was round? Well, actually Suzy, the theory the world is round is a very old one."
		},
		{
			"timestamps": {
				"from": "00:20:24,640",
				"to": "00:20:30,320"
			},
			"offsets": {
				"from": 1224640,
				"to": 1230320
			},
			"text": " In fact, it was during Aristotle's life that some of his fellow Greek scientist realized the earth"
		},
		{
			"timestamps": {
				"from": "00:20:30,320",
				"to": "00:20:36,640"
			},
			"offsets": {
				"from": 1230320,
				"to": 1236640
			},
			"text": " had to be round. In many ways, this idea of a round earth was the first step toward our"
		},
		{
			"timestamps": {
				"from": "00:20:36,640",
				"to": "00:20:41,760"
			},
			"offsets": {
				"from": 1236640,
				"to": 1241760
			},
			"text": " modern understanding of gravity. And Brahma Gupta took that a step further,"
		},
		{
			"timestamps": {
				"from": "00:20:41,760",
				"to": "00:20:49,360"
			},
			"offsets": {
				"from": 1241760,
				"to": 1249360
			},
			"text": " realizing there was gravity within the sphere of the earth. Now, Aristotle was right to, in a sense,"
		},
		{
			"timestamps": {
				"from": "00:20:49,360",
				"to": "00:20:56,800"
			},
			"offsets": {
				"from": 1249360,
				"to": 1256800
			},
			"text": " things can fall at different speeds. But, uh, that's because of differences in air resistance,"
		},
		{
			"timestamps": {
				"from": "00:20:56,800",
				"to": "00:21:05,200"
			},
			"offsets": {
				"from": 1256800,
				"to": 1265200
			},
			"text": " the atmosphere or counteracting gravity when it hits things that are not so compact, not dense."
		},
		{
			"timestamps": {
				"from": "00:21:05,840",
				"to": "00:21:11,760"
			},
			"offsets": {
				"from": 1265840,
				"to": 1271760
			},
			"text": " Aristotle, Ramag Gupta, other ancient thinkers, were missing an important theory. Well,"
		},
		{
			"timestamps": {
				"from": "00:21:11,760",
				"to": "00:21:18,240"
			},
			"offsets": {
				"from": 1271760,
				"to": 1278240
			},
			"text": " a fact. I'm talking about heliocentrism, the idea the earth isn't the center of the universe,"
		},
		{
			"timestamps": {
				"from": "00:21:18,240",
				"to": "00:21:25,680"
			},
			"offsets": {
				"from": 1278240,
				"to": 1285680
			},
			"text": " that it revolves around the sun. That idea became popular much later in the 1500s."
		},
		{
			"timestamps": {
				"from": "00:21:25,680",
				"to": "00:21:33,200"
			},
			"offsets": {
				"from": 1285680,
				"to": 1293200
			},
			"text": " Does anyone know who Copernicus is? Roger? He said the earth revolved around the sun,"
		},
		{
			"timestamps": {
				"from": "00:21:34,160",
				"to": "00:21:39,680"
			},
			"offsets": {
				"from": 1294160,
				"to": 1299680
			},
			"text": " but didn't he get in trouble for that? Didn't the church make him stop saying it?"
		},
		{
			"timestamps": {
				"from": "00:21:39,680",
				"to": "00:21:46,320"
			},
			"offsets": {
				"from": 1299680,
				"to": 1306320
			},
			"text": " Well, he wasn't punished, but he did get a lot of grief from religious leaders at the time."
		},
		{
			"timestamps": {
				"from": "00:21:46,320",
				"to": "00:21:51,600"
			},
			"offsets": {
				"from": 1306320,
				"to": 1311600
			},
			"text": " The idea certainly wasn't traditional, but other scientists and the public,"
		},
		{
			"timestamps": {
				"from": "00:21:51,600",
				"to": "00:21:57,760"
			},
			"offsets": {
				"from": 1311600,
				"to": 1317760
			},
			"text": " they embraced his ideas about planetary orbits. This new scientific attention to orbits set the"
		},
		{
			"timestamps": {
				"from": "00:21:57,760",
				"to": "00:22:04,000"
			},
			"offsets": {
				"from": 1317760,
				"to": 1324000
			},
			"text": " stage for Newton to realize that gravity made things fall to the earth, but they also made the moon"
		},
		{
			"timestamps": {
				"from": "00:22:04,000",
				"to": "00:22:09,280"
			},
			"offsets": {
				"from": 1324000,
				"to": 1329280
			},
			"text": " circle the earth, and then Newton figured out what we all know now."
		},
		{
			"timestamps": {
				"from": "00:22:09,280",
				"to": "00:22:13,120"
			},
			"offsets": {
				"from": 1329280,
				"to": 1333120
			},
			"text": " Larger objects have gravitational power over smaller ones."
		},
		{
			"timestamps": {
				"from": "00:22:13,120",
				"to": "00:22:19,920"
			},
			"offsets": {
				"from": 1333120,
				"to": 1339920
			},
			"text": " What aspect of gravitational science is the lecture mainly about?"
		},
		{
			"timestamps": {
				"from": "00:22:19,920",
				"to": "00:22:42,880"
			},
			"offsets": {
				"from": 1339920,
				"to": 1362880
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:22:42,880",
				"to": "00:22:48,400"
			},
			"offsets": {
				"from": 1362880,
				"to": 1368400
			},
			"text": " According to the professor, what two important things did the Indian science"
		},
		{
			"timestamps": {
				"from": "00:22:48,400",
				"to": "00:22:51,360"
			},
			"offsets": {
				"from": 1368400,
				"to": 1371360
			},
			"text": " Brahma Gupta realized about the earth?"
		},
		{
			"timestamps": {
				"from": "00:22:51,360",
				"to": "00:23:13,200"
			},
			"offsets": {
				"from": 1371360,
				"to": 1393200
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:23:13,200",
				"to": "00:23:19,040"
			},
			"offsets": {
				"from": 1393200,
				"to": 1399040
			},
			"text": " How did Copernicus' study of planetary orbits help scientists understand gravity?"
		},
		{
			"timestamps": {
				"from": "00:23:19,040",
				"to": "00:23:43,280"
			},
			"offsets": {
				"from": 1399040,
				"to": 1423280
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:23:43,280",
				"to": "00:23:47,520"
			},
			"offsets": {
				"from": 1423280,
				"to": 1427520
			},
			"text": " Listen again to part of the lecture. Then answer the question."
		},
		{
			"timestamps": {
				"from": "00:23:48,320",
				"to": "00:23:55,360"
			},
			"offsets": {
				"from": 1428320,
				"to": 1435360
			},
			"text": " Yeah, I guess. I just thought Aristotle thought flames kept going up and up and up."
		},
		{
			"timestamps": {
				"from": "00:23:55,360",
				"to": "00:24:02,320"
			},
			"offsets": {
				"from": 1435360,
				"to": 1442320
			},
			"text": " No, Aristotle thought the flames would stop at some point at their natural place in the sky,"
		},
		{
			"timestamps": {
				"from": "00:24:02,320",
				"to": "00:24:08,400"
			},
			"offsets": {
				"from": 1442320,
				"to": 1448400
			},
			"text": " but I can understand how you'd be confused. Aristotle's ideas seem odd to us today."
		},
		{
			"timestamps": {
				"from": "00:24:08,400",
				"to": "00:24:11,840"
			},
			"offsets": {
				"from": 1448400,
				"to": 1451840
			},
			"text": " Why does the professor say this?"
		},
		{
			"timestamps": {
				"from": "00:24:11,840",
				"to": "00:24:15,200"
			},
			"offsets": {
				"from": 1451840,
				"to": 1455200
			},
			"text": " Aristotle's ideas seem odd to us today."
		},
		{
			"timestamps": {
				"from": "00:24:15,200",
				"to": "00:24:17,200"
			},
			"offsets": {
				"from": 1455200,
				"to": 1457200
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:24:17,200",
				"to": "00:24:46,160"
			},
			"offsets": {
				"from": 1457200,
				"to": 1486160
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:24:46,160",
				"to": "00:24:51,120"
			},
			"offsets": {
				"from": 1486160,
				"to": 1491120
			},
			"text": " Listen again to part of the lecture. Then answer the question."
		},
		{
			"timestamps": {
				"from": "00:24:51,120",
				"to": "00:24:56,720"
			},
			"offsets": {
				"from": 1491120,
				"to": 1496720
			},
			"text": " In fact, it was during Aristotle's life that some of his fellow Greek scientist realized the earth"
		},
		{
			"timestamps": {
				"from": "00:24:56,720",
				"to": "00:25:03,120"
			},
			"offsets": {
				"from": 1496720,
				"to": 1503120
			},
			"text": " had to be round. In many ways, this idea of a round earth was the first step toward our"
		},
		{
			"timestamps": {
				"from": "00:25:03,120",
				"to": "00:25:05,600"
			},
			"offsets": {
				"from": 1503120,
				"to": 1505600
			},
			"text": " modern understanding of gravity."
		},
		{
			"timestamps": {
				"from": "00:25:05,600",
				"to": "00:25:08,640"
			},
			"offsets": {
				"from": 1505600,
				"to": 1508640
			},
			"text": " What does the professor imply when he says this?"
		},
		{
			"timestamps": {
				"from": "00:25:09,520",
				"to": "00:25:15,200"
			},
			"offsets": {
				"from": 1509520,
				"to": 1515200
			},
			"text": " In fact, it was during Aristotle's life that some of his fellow Greek scientist realized the earth"
		},
		{
			"timestamps": {
				"from": "00:25:15,200",
				"to": "00:25:17,200"
			},
			"offsets": {
				"from": 1515200,
				"to": 1517200
			},
			"text": " had to be round."
		},
		{
			"timestamps": {
				"from": "00:25:17,200",
				"to": "00:25:25,200"
			},
			"offsets": {
				"from": 1517200,
				"to": 1525200
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:25:25,200",
				"to": "00:25:47,200"
			},
			"offsets": {
				"from": 1525200,
				"to": 1547200
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:25:47,200",
				"to": "00:25:52,160"
			},
			"offsets": {
				"from": 1547200,
				"to": 1552160
			},
			"text": " Match each gravitational theory below to the scientist who held the theory."
		},
		{
			"timestamps": {
				"from": "00:25:52,160",
				"to": "00:26:16,160"
			},
			"offsets": {
				"from": 1552160,
				"to": 1576160
			},
			"text": " [no audio]"
		},
		{
			"timestamps": {
				"from": "00:26:16,160",
				"to": "00:26:25,520"
			},
			"offsets": {
				"from": 1576160,
				"to": 1585520
			},
			"text": " For answers, explanations, and help scoring, go to www.mugusch.com/youtube listening answers."
		},
		{
			"timestamps": {
				"from": "00:26:25,520",
				"to": "00:26:34,320"
			},
			"offsets": {
				"from": 1585520,
				"to": 1594320
			},
			"text": " You're done! Good job! How'd you do? If you want to learn more strategies and learn how to answer these"
		},
		{
			"timestamps": {
				"from": "00:26:34,320",
				"to": "00:26:41,760"
			},
			"offsets": {
				"from": 1594320,
				"to": 1601760
			},
			"text": " questions, how to do the best on test day, come to mugusch.com. We have many more practice questions"
		},
		{
			"timestamps": {
				"from": "00:26:41,760",
				"to": "00:26:49,040"
			},
			"offsets": {
				"from": 1601760,
				"to": 1609040
			},
			"text": " just like this, and we have explanation videos for every single question that will tell you"
		},
		{
			"timestamps": {
				"from": "00:26:49,040",
				"to": "00:26:54,400"
			},
			"offsets": {
				"from": 1609040,
				"to": 1614400
			},
			"text": " how to answer them and how to avoid those wrong answers that tricked you."
		},
		{
			"timestamps": {
				"from": "00:26:54,400",
				"to": "00:27:00,800"
			},
			"offsets": {
				"from": 1614400,
				"to": 1620800
			},
			"text": " Come to mugusch.com and we can help you out. I hope you enjoyed this. Happy studying!"
		}
	]
    return jsonify(transcription_data)

if __name__ == '__main__':
    app.run(debug=True)
