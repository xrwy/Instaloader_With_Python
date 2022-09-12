from flask import Flask, render_template, request
import instaloader


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return render_template('user_login.html')

@app.route('/result', methods = ['GET','POST'])
def instaloaderResult():
    stateInfo = []

    if request.method == 'POST':
        userName = request.form['user_name']
        userNames = userName.split(',')
        if len(userNames) == 1:
            try:
                insagram = instaloader.Instaloader()
                insagram.download_profile(userName, profile_pic_only=True)

                stateInfo.append([True,userName, 'Successfull'])

            except Exception as e:
                stateInfo.append([False, userName, 'Not Successfull'])

            return render_template('result.html', state_info = stateInfo)

        else:
            userNames = userName.split(',')
            for user in userNames:
                try:
                    insagram = instaloader.Instaloader()
                    insagram.download_profile(user, profile_pic_only=True)
                    stateInfo.append([True,user, 'Successfull'])

                except Exception as e:
                    stateInfo.append([False, user, 'Not Successfull'])

            return render_template('result.html', state_info = stateInfo)
    else:
        return 'For post requests only.'


if __name__ == '__main__':
    app.run(debug=True, port=5000)