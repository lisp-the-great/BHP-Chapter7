require 'inline'

class XScreenSaver
  class << self
    inline do |builder|
      builder.add_link_flags 'lXss' 'lX11'
      builder.include '<X11/extensions/scrnsaver.h>'
      builder.c %{
        double idle_time() {
          static Display *display;
          XScreenSaverInfo *info = XScreenSaverAllocInfo();
          if (!display) display = XOpenDisplay(0);
          if (!display) return -1;
          XScreenSaverQueryInfo(display, DefaultRootWindow(display), info);
          return info->idle / 1000.0;
        }
      }
    end
  end
end

if __FILE__ == $0
  loop { puts XScreenSaver.idle_time; sleep 0.2 }
end