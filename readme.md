# My Kivy Android App

A simple Android application built with Kivy Python framework, automatically compiled using GitHub Actions.

## Features

- Text input and display functionality
- Current time display
- Simple UI interactions
- Clean, modern interface
- Popup notifications

## Files Structure

```
your-repo/
├── main.py                 # Main application code
├── buildozer.spec         # Build configuration
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .github/
    └── workflows/
        └── build.yml     # GitHub Actions workflow
```

## Setup Instructions

### 1. Create a New GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Clone it to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

### 2. Add the Files

Create these files in your repository with the provided code:

- `main.py` - The main application code
- `buildozer.spec` - Build configuration file
- `requirements.txt` - Python dependencies
- `.github/workflows/build.yml` - GitHub Actions workflow
- `README.md` - This documentation

### 3. Commit and Push

```bash
# Add all files
git add .

# Commit the files
git commit -m "Initial commit: Kivy Android app"

# Push to GitHub
git push origin main
```

### 4. Enable GitHub Actions

1. Go to your GitHub repository
2. Click on the "Actions" tab
3. GitHub Actions should automatically detect the workflow file
4. The build will start automatically on push

### 5. Download Your APK

Once the build completes:

1. Go to the "Actions" tab in your GitHub repository
2. Click on the latest build
3. Scroll down to "Artifacts"
4. Download the "android-apk" file
5. Extract the ZIP to get your APK file

Alternatively, if you pushed to the main branch, check the "Releases" section for automatically created releases with APK files.

## Customization

### Changing App Details

Edit `buildozer.spec`:
- `title`: Your app name
- `package.name`: Package identifier (lowercase, no spaces)
- `package.domain`: Your domain (e.g., com.yourname)

### Modifying the App

Edit `main.py` to customize:
- UI layout and design
- Button functionality
- App features and behavior

### Adding Dependencies

Add any additional Python packages to `requirements.txt` and update the `requirements` line in `buildozer.spec`.

## Local Testing (Optional)

To test locally on Windows (if you want to test the Python code):

```bash
# Install Python dependencies
pip install kivy kivymd

# Run the app
python main.py
```

Note: This will only run the Python/Kivy app in a desktop window, not as an Android app.

## Troubleshooting

### Build Fails
- Check the Actions log for specific errors
- Ensure all file names are correct
- Verify the buildozer.spec configuration

### APK Won't Install
- Enable "Install from Unknown Sources" on your Android device
- Check that the APK downloaded completely
- Try installing via ADB: `adb install your-app.apk`

### App Crashes
- Check the main.py code for syntax errors
- Ensure all imported modules are included in requirements

## Building Process

The GitHub Actions workflow:
1. Sets up Ubuntu environment
2. Installs Android SDK, NDK, and build tools
3. Installs Python dependencies
4. Runs Buildozer to compile the APK
5. Uploads the APK as an artifact
6. Creates a release (for main branch pushes)

This process typically takes 15-30 minutes depending on whether dependencies are cached.

## License

This project is open source and available under the MIT License.